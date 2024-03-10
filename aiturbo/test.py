import numpy


def lsqnonneg(C, d, x0=None, tol=None, itmax_factor=3):
    '''Linear least squares with nonnegativity constraints.
    (x, resnorm, residual) = lsqnonneg(C,d) returns the vector x that minimizes norm(d-C*x)
    subject to x >= 0, C and d must be real
    '''

    eps = 2.22e-16  # from matlab

    def norm1(x):
        return abs(x).sum().max()

    def msize(x, dim):
        s = x.shape
        if dim >= len(s):
            return 1
        else:
            return s[dim]

    if tol is None: tol = 10 * eps * norm1(C) * (max(C.shape) + 1)

    C = numpy.asarray(C)

    (m, n) = C.shape
    P = numpy.zeros(n)
    Z = numpy.arange(1, n + 1)

    if x0 is None:
        x = P
    else:
        if any(x0 < 0):
            x = P
        else:
            x = x0

    ZZ = Z

    resid = d - numpy.dot(C, x)
    w = numpy.dot(C.T, resid)

    outeriter = 0;
    it = 0
    itmax = itmax_factor * n
    exitflag = 1

    # outer loop to put variables into set to hold positive coefficients
    while numpy.any(Z) and numpy.any(w[ZZ - 1] > tol):
        outeriter += 1

        t = w[ZZ - 1].argmax()
        t = ZZ[t]

        P[t - 1] = t
        Z[t - 1] = 0

        PP = numpy.where(P != 0)[0] + 1
        ZZ = numpy.where(Z != 0)[0] + 1

        CP = numpy.zeros(C.shape)

        CP[:, PP - 1] = C[:, PP - 1]
        CP[:, ZZ - 1] = numpy.zeros((m, msize(ZZ, 1)))

        z = numpy.dot(numpy.linalg.pinv(CP), d)

        z[ZZ - 1] = numpy.zeros((msize(ZZ, 1), msize(ZZ, 0)))

        # inner loop to remove elements from the positve set which no longer belong
        while numpy.any(z[PP - 1] <= tol):
            it += 1

            if it > itmax:
                max_error = z[PP - 1].max()
                raise Exception('Exiting: Iteration count (=%d) exceeded\n Try raising the \
                                 tolerance tol. (max_error=%d)' % (it, max_error))

            QQ = numpy.where((z <= tol) & (P != 0))[0]
            alpha = min(x[QQ] / (x[QQ] - z[QQ]))
            x = x + alpha * (z - x)

            ij = numpy.where((abs(x) < tol) & (P != 0))[0] + 1
            Z[ij - 1] = ij
            P[ij - 1] = numpy.zeros(max(ij.shape))
            PP = numpy.where(P != 0)[0] + 1
            ZZ = numpy.where(Z != 0)[0] + 1

            CP[:, PP - 1] = C[:, PP - 1]
            CP[:, ZZ - 1] = numpy.zeros((m, msize(ZZ, 1)))

            z = numpy.dot(numpy.linalg.pinv(CP), d)
            z[ZZ - 1] = numpy.zeros((msize(ZZ, 1), msize(ZZ, 0)))

        x = z
        resid = d - numpy.dot(C, x)
        w = numpy.dot(C.T, resid)

    return x, sum(resid * resid), resid


if __name__ == '__main__':
    v = [[32, 1, 1, 1.9083558209330604, 1, 1, 1], [32, 1, 1, 1.9083558209330604, 1, 1, 2], [16.0, 1, 2, 3.816711641866121, 2, 1, 2], [10.666666666666666, 1, 3, 5.725067462799181, 3, 1, 3], [32, 1, 0.5, 0.9541779104665302, 1, 2, 1], [32, 1, 0.5, 0.9541779104665302, 1, 2, 2], [16.0, 1, 1, 1.9083558209330604, 2, 2, 2]]
    C = numpy.array(v)

    d = numpy.array([0.3370531327303496, 0.3433476394849786, 0.1694915254237288, 0.03389830508474576, 0.3347280334728034, 0.33755274261603374, 0.16877637130801687])

    alpha = numpy.linalg.lstsq(C, d, rcond=None)[0]
    string = ""
    for i in range(len(alpha)):
        string = string + "\t" + str(alpha[i])
    print(string)
    # [x, resnorm, residual] = lsqnonneg(C, d)
    # dres = abs(resnorm - 0.8315)          # compare with matlab result
    # print('ok, diff:', dres)
    # if dres > 0.001:
    #     raise Exception('Error')
    # print([x, resnorm, residual])

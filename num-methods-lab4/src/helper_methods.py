# Делит строки системы
def divide_row(A, f, row, divider):
    A[row] = [a / divider for a in A[row]]
    f[row] /= divider


# Прибавляет к строке другую строку, умноженную на коэффициент
def combine_rows(A, f, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    f[row] += f[source_row] * weight

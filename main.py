def main():
    table = [
        [200, 140, 170, 145, 165],
        [190, 150, 210, 150, 150],
        [230, 190, 200, 190, 200],
        [150, 170, 150, 170, 180]
    ]
    factors = 5
    experiments = 4
    alpha = 0.05
    values = factors * experiments

    print('Analysis of variance')
    # degrees of freedom
    print('degrees of freedom')
    v1 = factors - 1
    v2 = values - factors
    v3 = experiments - 1
    print(v1, v2, v3)

    # groups average
    print('groups average')
    groups_average = []
    for factor in range(factors):
        summary = 0
        for exp in range(experiments):
            summary += table[exp][factor]
        groups_average.append(summary / experiments)
    print(groups_average)

    # average x
    print('average x')
    average_x = sum(groups_average) / factors
    print(f'average x: {average_x}')

    # sums
    print('sums')
    full_sum = 0
    for i in range(experiments):
        for j in range(factors):
            full_sum += (table[i][j] - average_x)**2
    print(f'full sum: {full_sum}')

    factors_sum = 0
    for i in range(factors):
        factors_sum += (groups_average[i] - average_x)**2
    factors_sum *= experiments
    print(f'factors sum: {factors_sum}')

    residual_sum = full_sum - factors_sum
    print(f'residual sum: {residual_sum}')

    # dispersions
    print('dispersions')
    factors_sum_dispersion = 1.0 * factors_sum / (factors - 1)
    residual_sum_dispersion = 1.0 * residual_sum / factors / (experiments - 1)
    print(f'factors sum dispersion: {factors_sum_dispersion}')
    print(f'residual sum dispersion: {residual_sum_dispersion}')

    # Fisher's actual attitude
    print('Fisher\'s actual attitude')
    f_attitude = factors_sum_dispersion / residual_sum_dispersion
    print(f_attitude)

    # Critical value
    print('Fisher\'s critical value')
    f_critical = 3.06
    print(f_critical)

    if f_attitude >= f_critical:
        print('Влияет на результат')
    else:
        print('Не влияет на результат')


if __name__ == '__main__':
    main()

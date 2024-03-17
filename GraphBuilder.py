from matplotlib import pyplot
import numexpr


def function_value_list(start_val, step_val, stop_val):
    result_list = []
    v = start_val
    while v <= stop_val:
        result_list.append(round(v, 2))
        v += step_val
    return result_list


while True:
    function = ''
    while function == '':
        function = input('Input your function:')
        if function == '':
            print('Function can not be empty')

    start, stop = -50, 50
    interval = '0'
    while interval == '0':
        interval = input('The default rendering interval is [-50;50]. Press ENTER if this value suits you. If not, \
enter the interval value manually:')
        if interval == '0':
            print('Rendering Interval can not be empty')
    if interval != '':
        interval_range_list = [-int(interval), int(interval)]
        start, stop = min(interval_range_list), max(interval_range_list)

    step = 0.01
    string_step = '0'
    while string_step == '0':
        string_step = input('Function step by default == 0.01. Press ENTER if this value suits you. If not - enter the\
step value manually:')
        if string_step == '0':
            print('Function step can not be empty')
    if string_step != '':
        step = float(string_step)

    x = function_value_list(start, step, stop)

    y = numexpr.evaluate(function)
    for i in range(len(y)):
        y[i] = round(y[i], 2)
        if abs(y[i]) > abs(start * stop):
            y[i] = None

    fig, ax = pyplot.subplots()
    ax.plot(x, y)
    ax.grid()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    pyplot.plot(x, y)
    ax = pyplot.gca()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    ax.plot(x, y, label=function)
    ax.legend()
    fig.set_figheight(8)
    fig.set_figheight(5)

    pyplot.show()

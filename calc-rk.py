# MSSERG | 12:00 MSC 20.01.2018

print('''Калькулятор:
\nРасчет квартплаты состоит из следующих показателей:
• плата за потреблённые коммунальные услуги;
• взносы на ремонт и содержание.
Кроме этого наниматели муниципального жилья платят
за наём (пользование квартирой), а собственники
вносят взносы на капитальный ремонт дома.
С 2012 года комммунальные платежи стали делиться
на две части: потребление каждой квартирой отдельно
и общедомовые нужды. Сумма платежа=N*T*L, где:
N-норматив на одного человека, T-тариф на данную услугу,
L-количество прописанных в квартире граждан. При наличии
счётчиков, платить только за использованный ресурс.\n''')

N = float(input('Норматив на одного человека(N): '))
T = float(input('Тариф на данную услугу (T): '))
L = float(input('Количество прописанных в квартире граждан (L): '))
summPay = 0; summPay = N*T*L;

print('Сумма платежа квартплаты =', summPay, 'руб.')

input('\nПауза для консоли.')
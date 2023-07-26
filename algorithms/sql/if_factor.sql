SELECT id,
(CASE
  WHEN MOD(base, factor) = 0 THEN
  true
  ELSE false END) AS res
FROM kata

--Эта функция должна проверить, является ли коэффициент коэффициентом основания.
--
--Возвращает true, если фактор является фактором, или false, если не является.
--
--О факторах
--Факторы - это числа, которые можно умножить друг на друга, чтобы получить другое число.
--
--2 и 3 являются коэффициентами числа 6, потому что: 2 * 3 = 6
--
--Фактор можно найти путем деления чисел. Если остаток равен 0, то число является множителем.
--В большинстве языков для проверки наличия остатка можно использовать оператор mod (%).
--Например, 2 не является множителем числа 7, так как: 7 % 2 = 1
--
--Примечание: основание - неотрицательное число, множитель - положительное число.


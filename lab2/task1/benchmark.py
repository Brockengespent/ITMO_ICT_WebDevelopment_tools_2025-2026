"""
Сравнительный бенчмарк всех трёх подходов для Задачи 1.
Запускает threading, multiprocessing и async последовательно
и выводит таблицу с временем выполнения.
"""

import threading_solution
import multiprocessing_solution
import async_solution

N = 10_000_000  # Менять здесь для теста разных значений


def run_benchmark():
    print("=" * 55)
    print(f"  БЕНЧМАРК: сумма чисел 1..{N:,}")
    print("=" * 55)

    t_threading = threading_solution.main(N)
    t_multiprocessing = multiprocessing_solution.main(N)
    t_async = async_solution.main(N)

    print("=" * 55)
    print(f"  {'Подход':<25} {'Время (сек)':>12}")
    print("-" * 55)
    print(f"  {'Threading':<25} {t_threading:>12.4f}")
    print(f"  {'Multiprocessing':<25} {t_multiprocessing:>12.4f}")
    print(f"  {'Async + ProcessPool':<25} {t_async:>12.4f}")
    print("=" * 55)

    fastest = min(t_threading, t_multiprocessing, t_async)
    names = {
        t_threading: "Threading",
        t_multiprocessing: "Multiprocessing",
        t_async: "Async + ProcessPool",
    }
    print(f"\n  Победитель: {names[fastest]} ({fastest:.4f} сек)")


if __name__ == "__main__":
    run_benchmark()

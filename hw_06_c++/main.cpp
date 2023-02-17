
// 1. Программа, которая сравнивает два введённых с клавиатуры числа. Программа указывет, какое число больше или, если числа равны, выводит соответствующее сообщение
#include <iostream>
using namespace std;

int main() {
  int num1, num2;

  cout << "Введите первое число: ";
  cin >> num1;

  cout << "Введите второе число: ";
  cin >> num2;

  if (num1 > num2) {
    cout << num1 << " больше, чем " << num2 << endl;
  }
  else if (num2 > num1) {
    cout << num2 << " больше, чем " << num1 << endl;
  }
  else {
    cout << "Числа равны" << endl;
  }

  return 0;
}


// 2. Программа, которая проверяет является ли год високосным
#include <iostream>
using namespace std;

int main() {
  int year;

  cout << "Введите год: ";
  cin >> year;

  if (year % 4 == 0) {
    if (year % 100 == 0) {
      if (year % 400 == 0) {
        cout << year << " - високосный год" << endl;
      }
      else {
        cout << year << " - не високосный год" << endl;
      }
    }
    else {
      cout << year << " - високосный год" << endl;
    }
  }
  else {
    cout << year << " - не високосный год" << endl;
  }

  return 0;
}


// 3. Программа для решения квадратного уравнения. Программа проверяет правильность исходных данных и в случае, если коэффициент при второй степени неизвестного равен нулю, выводить соответствующее сообщение
#include <iostream>
#include <cmath>
using namespace std;

int main() {
  double a, b, c, discriminant, root1, root2;

  cout << "Введите коэффициент a: ";
  cin >> a;

  if (a == 0) {
    cout << "Ошибка: коэффициент при второй степени неизвестного не может быть равен нулю." << endl;
    return 0;
  }

  cout << "Введите коэффициент b: ";
  cin >> b;

  cout << "Введите коэффициент c: ";
  cin >> c;

  discriminant = pow(b, 2) - 4 * a * c;

  if (discriminant > 0) {
    root1 = (-b + sqrt(discriminant)) / (2 * a);
    root2 = (-b - sqrt(discriminant)) / (2 * a);
    cout << "Корни уравнения: " << root1 << " и " << root2 << endl;
  }
  else if (discriminant == 0) {
    root1 = -b / (2 * a);
    cout << "Уравнение имеет единственный корень: " << root1 << endl;
  }
  else {
    cout << "Уравнение не имеет действительных корней." << endl;
  }

  return 0;
}


// 4. Программа на C++, которая проверяет на чётность введённое с клавиатуры число 
#include <iostream>
using namespace std;

int main() {
  int number;

  cout << "Введите число: ";
  cin >> number;

  if (number % 2 == 0) {
    cout << "Число " << number << " четное." << endl;
  }
  else {
    cout << "Число " << number << " нечетное." << endl;
  }

  return 0;
}


// 5. Программа, которая выводит таблицу квадратов десяти первых положительных чисел
#include <iostream>
using namespace std;

int main() {
  for (int i = 1; i <= 10; i++) {
    cout << "Квадрат числа " << i << " = " << i * i << endl;
  }

  return 0;
}


//6. Программа, которая определяет максимальное число из введённой с клавиатуры последовательности положительных чисел (длина последовательности неограниченна) 
#include <iostream>
using namespace std;

int main() {
  int number;
  int max = 0; // начальное максимальное значение

  do {
    cout << "Введите положительное число (для завершения введите 0): ";
    cin >> number;

    if (number > max) {
      max = number; // обновляем максимальное значение
    }

  } while (number > 0); // цикл продолжается, пока пользователь вводит положительные числа

  cout << "Максимальное число: " << max << endl;

  return 0;
}


// 7. Программа, которая выводит таблицу значений функции y=-2 * x^2 - 5 * x - 8 в диапазоне от –4 до +4, с шагом 0,5 
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double x = -4.0;
    while (x <= 4.0) {
        double y = -2 * pow(x, 2) - 5 * x - 8;
        cout << "x = " << x << ", y = " << y << endl;
        x += 0.5;
    }
    return 0;
}


// 8. Программа создает двумерный массив 5 х 5. Написана функция, которая заполняет массив случайными числами от 30 до 60. Написаны еще две функции, которые находят максимальный и минимальный элементы этого двумерного массива
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void fillArray(int array[5][5]) {
    srand(time(NULL));
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            array[i][j] = rand() % 31 + 30;
        }
    }
}

int findMax(int array[5][5]) {
    int max = array[0][0];
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (array[i][j] > max) {
                max = array[i][j];
            }
        }
    }
    return max;
}

int findMin(int array[5][5]) {
    int min = array[0][0];
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (array[i][j] < min) {
                min = array[i][j];
            }
        }
    }
    return min;
}

int main() {
    int myArray[5][5];
    fillArray(myArray);

    cout << "Array: " << endl;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cout << myArray[i][j] << " ";
        }
        cout << endl;
    }

    int max = findMax(myArray);
    int min = findMin(myArray);

    cout << "Max value: " << max << endl;
    cout << "Min value: " << min << endl;

    return 0;
}


// 9. Создана структура с именем student, содержащая поля: фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов). Создан массив из десяти элементов такого типа, упорядочнены записи по возрастанию среднего балла. Добавлена возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Структура для хранения информации о студенте
struct student {
    string name; // Фамилия и инициалы
    int group; // Номер группы
    int grades[5]; // Успеваемость (оценки по 5 предметам)

    // Метод для вычисления среднего балла
    double average_grade() const {
        double sum = 0;
        for (int i = 0; i < 5; i++) {
            sum += grades[i];
        }
        return sum / 5;
    }

    // Метод для проверки, имеет ли студент только оценки 4 и 5
    bool has_only_good_grades() const {
        for (int i = 0; i < 5; i++) {
            if (grades[i] < 4) {
                return false;
            }
        }
        return true;
    }
};

// Функция для сравнения студентов по среднему баллу
bool compare_students(const student& a, const student& b) {
    return a.average_grade() < b.average_grade();
}

int main() {
    // Создание массива студентов
    student students[10] = {
        {"Иванов А.С.", 1, {4, 5, 4, 5, 5}},
        {"Петров В.В.", 2, {3, 4, 5, 4, 4}},
        {"Сидоров С.П.", 1, {4, 4, 4, 4, 4}},
        {"Кузнецов Д.А.", 2, {5, 5, 5, 5, 5}},
        {"Смирнова Е.Н.", 1, {4, 4, 4, 4, 4}},
        {"Федорова И.В.", 2, {5, 4, 5, 4, 5}},
        {"Соколова Н.М.", 1, {5, 5, 5, 5, 5}},
        {"Исаева М.С.", 2, {4, 4, 4, 4, 4}},
        {"Королева О.Н.", 1, {4, 4, 4, 4, 4}},
        {"Васильева П.В.", 2, {5, 5, 5, 5, 5}}
    };

    // Сортировка студентов по среднему баллу
    sort(students, students + 10, compare_students);

    // Вывод фамилий и номеров групп студентов с оценками только 4 и 5
    cout << "Студенты с оценками только 4 и 5:" << endl;
    for (int i = 0; i < 10; i++) {
        if (students[i].has_only_good_grades()) {
            cout << students[i].name << ", группа " << students[i].group << endl;
        }
    }

    return 0;
}


// 10. Создана структура с именем train, содержащая поля: название пункта назначения, номер поезда, время отправления. Введены данные в массив из пяти элементов типа train, упорядочены элементы по номерам поездов. Добавлена возможность вывода информации о поезде, номер которого введен пользователем. Добавлена возможность сортировки массива по пункту назначения, причем поезда с одинаковыми пунктами назначения упорядочены по времени отправления
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Определение структуры Train
struct Train {
    string destination;
    int number;
    string departure_time;
};

// Функция для сортировки по номерам поездов
bool sortByNumber(const Train& t1, const Train& t2) {
    return t1.number < t2.number;
}

// Функция для сортировки по пункту назначения и времени отправления
bool sortByDestination(const Train& t1, const Train& t2) {
    if (t1.destination == t2.destination) {
        return t1.departure_time < t2.departure_time;
    }
    return t1.destination < t2.destination;
}

int main() {
    // Создание массива из пяти элементов типа Train
    Train trains[5];

    // Ввод данных о поездах
    for (int i = 0; i < 5; i++) {
        cout << "Введите название пункта назначения для поезда " << i+1 << ": ";
        cin >> trains[i].destination;
        cout << "Введите номер поезда: ";
        cin >> trains[i].number;
        cout << "Введите время отправления в формате 'чч:мм': ";
        cin >> trains[i].departure_time;
        cout << endl;
    }

    // Сортировка по номерам поездов
    sort(trains, trains+5, sortByNumber);

    // Вывод информации о поезде по номеру
    int searchNumber;
    cout << "Введите номер поезда для поиска: ";
    cin >> searchNumber;
    for (int i = 0; i < 5; i++) {
        if (trains[i].number == searchNumber) {
            cout << "Информация о поезде:" << endl;
            cout << "Название пункта назначения: " << trains[i].destination << endl;
            cout << "Номер поезда: " << trains[i].number << endl;
            cout << "Время отправления: " << trains[i].departure_time << endl;
            cout << endl;
            break;
        }
    }

    // Сортировка по пункту назначения и времени отправления
    sort(trains, trains+5, sortByDestination);

    // Вывод информации о поездах, отсортированных по пункту назначения и времени отправления
    cout << "Список поездов, отсортированных по пункту назначения и времени отправления:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Название пункта назначения: " << trains[i].destination << endl;
        cout << "Номер поезда: " << trains[i].number << endl;
        cout << "Время отправления: " << trains[i].departure_time << endl;
        cout << endl;
    }

    return 0;
}


package org.example

import scala.io.StdIn.readLine

object App {

  def taskA(varStr: String): (String, String, String, String) = {
    // a.i. выводит фразу «Hello, Scala!» справа налево
    val varStrRev = varStr.reverse

    // a.ii. переводит всю фразу в нижний регистр
    val varStrLow = varStr.toLowerCase()

    // a.iii. удаляет символ!
    val varStrRep = varStr.replace("!", "")

    // a.iv. добавляет в конец фразы «and goodbye python!»
    val varStrCon = varStr.concat(" and goodbye python!")

    (varStrRev, varStrLow, varStrRep, varStrCon)
  }


  def taskB(yearSalary: Float, bonus: Float, compensation: Float): Double = {
    // Напишите программу, которая вычисляет ежемесячный оклад сотрудника после вычета налогов.
    // На вход вашей программе подается значение годового дохода до вычета налогов, размер премии –
    // в процентах от годового дохода и компенсация питания.

    val monthlySalary = (yearSalary * bonus + compensation + yearSalary) * 0.87

    monthlySalary
  }


  def taskC(bonus: Float, compensation: Float, salariesList: List[Int]): List[Double] = {
    // Напишите программу, которая рассчитывает для каждого сотрудника отклонение(в процентах) от среднего значения
    // оклада на уровень всего отдела. В итоговом значении должно учитываться в большую или меньшую сторону отклоняется
    // размер оклада. На вход вашей программе подаются все значения, аналогичные предыдущей программе, а также список со
    // значениями окладов сотрудников отдела 100, 150, 200, 80, 120, 75.

    // из задания b
    var newEmployee = List[Double]()

    for (elem <- salariesList) {
      newEmployee = (elem * bonus + compensation + elem) * 0.87 +: newEmployee
    }

    // среднее
    val avgSalary = newEmployee.sum / newEmployee.length

    // расчет отклонения от среднего
    var deviation = List[Double]()
    for (elem <- newEmployee) {
      deviation = (100 * (elem - avgSalary) / avgSalary) +: deviation
    }
    deviation
  }


  def taskD(employeeSalary: Double, deviation: List[Double], behavior: String): (Double, Double) = {
    // Попробуйте рассчитать новую зарплату сотрудника, добавив(или отняв, если сотрудник плохо себя вел) необходимую
    // сумму с учетом результатов прошлого задания. Добавьте его зарплату в список и вычислите значение самой высокой
    // зарплаты и самой низкой.

    var newSalaryNewEmployee = List[Double]()

    for (elem <- deviation) {
      if (behavior == "good") {
        newSalaryNewEmployee = (employeeSalary + elem) +: newSalaryNewEmployee
      } else {
        newSalaryNewEmployee = (employeeSalary - elem) +: newSalaryNewEmployee
      }
    }

    // значение самой высокой и самой низкой зарплаты
    (newSalaryNewEmployee.min, newSalaryNewEmployee.max)
  }


  def taskE(employeeOne: Int, employeeTwo: Int, salariesList: List[Int]): List[Int] = {
    // Также в вашу команду пришли два специалиста с окладами 350 и 90 тысяч рублей. Попробуйте отсортировать список
    // сотрудников по уровню оклада от меньшего к большему.

    var resultSalariesList = salariesList

    resultSalariesList :+= employeeOne

    resultSalariesList :+= employeeTwo

    resultSalariesList.sorted
  }


  def taskF(employeeOther: Int, salariesList: List[Int]): List[Int] = {
    // Кажется, вы взяли в вашу команду еще одного сотрудника и предложили ему оклад 130 тысяч. Вычислите самостоятельно
    // номер сотрудника в списке так, чтобы сортировка не нарушилась и добавьте его на это место.

    var indexNew = 0
    for (i <- salariesList.indices) {
      if (salariesList(i) < employeeOther) {
        indexNew = i
      }
    }

    // разбили на части
    val part = salariesList.splitAt(indexNew)

    // соединили
    val sortedList = part._1 ++ List(employeeOther) ++ part._2

    // отсортировали
    sortedList.sorted
  }


  def taskG(salariesList: List[Int], minSalary: Float, maxSalary: Float): List[Int] = {
    // Попробуйте вывести номера сотрудников из полученного списка, которые попадают под категорию middle. На входе
    // программе подается «вилка» зарплаты специалистов уровня middle.

    var numMiddle = List[Int]()
    for (elem <- salariesList) {
      if ((elem >= minSalary) && (elem <= maxSalary)) numMiddle = elem +: numMiddle
    }
    numMiddle
  }


  def taskH(salariesList: List[Int]): List[Float] = {
    // Однако наступил кризис и ваши сотрудники требуют повысить зарплату. Вам необходимо проиндексировать зарплату
    // каждого сотрудника на уровень инфляции – 7%

    var wageIndexation = List[Float]()
    for (elem <- salariesList) {
      wageIndexation = (elem * 1.07f) +: wageIndexation
    }
    wageIndexation.reverse
  }


  def main(args: Array[String]): Unit = {
    // пункт а
    println("Пункт a ", taskA("Hello, Scala!"))

    // пункт b
    val yearSalary = readLine("Введите годовой доход: ").toFloat
    val bonus = readLine("Размер премии: ").toFloat
    val compensation = readLine("Компенсация питания: ").toFloat
    println("Пункт b ", taskB(yearSalary, bonus, compensation))

    val listSalary: List[Int] = List(100, 150, 200, 80, 120, 75)

    // пункт c
    println("Пункт c ", taskC(bonus, compensation, listSalary))

    // пункт d
    val behavior = readLine("Поведение сотрудника (good или bad): ")
    println("Пункт d ", taskD(taskB(yearSalary, bonus, compensation), taskC(bonus, compensation, listSalary), behavior))

    // пункт e
    println("Пункт e ", taskE(350, 90, listSalary))

    // пункт f
    println("Пункт f ", taskF(130, listSalary))

    // пункт g
    println("Пункт g ", taskG(listSalary, 120, 200))

    // пункт h
    println("Пункт h ", taskH(listSalary))
  }
}
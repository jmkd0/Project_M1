import Foundation
//Exercices sur les boucles
//Question 1
func displayMessage(){
    print("Enter a message:")
    let message = readLine()!
    print("Enter a number:")
    let n = Int(readLine()!)!
    for _ in 1...n{
        print(message)
    }
}
//Question2
func calculateMean(){
    print("Calculate mean")
    var n = 0.0
    var mean = 0.0
    var value = 0.0
    repeat {
        print("Enter number type -1 to end:")
        value = Double(readLine()!)!
        mean += value
        n += 1
    }while(value != -1)
    mean += 1
    mean /= n-1
    print("The mean of those number is \(mean)")
}
//Question 3
func findMinimum(){
    print("Find the minimum")
    var min = 0.0
    var value = 0.0
    print("Enter number type -1 to end:")
    value = Double(readLine()!)!
    min = value
    repeat {
        print("Enter number type -1 to end:")
        value = Double(readLine()!)!
        if value < min && value != -1{
            min = value
        }
    }while(value != -1)
    print("The mean of those number is \(min)")
}

//Exercice 1
func exercie1(){
    let list = ["un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix"]
    for i in 0...list.count-1{
        print("\(list[i])")
    }
    let first = list[0]
    let last = list[list.count-1]
    print("The fist element is \(first)")
    print("The last element is \(last)")
    var list1 = [String]()
    for i in stride(from:list.count, to: 0, by: -1){
        list1.append(list[i-1])
    }
    
}
//Exercice 2
func concatChain(){
    let chain1 = "one"
    let chain2 = "two"
    let concat = chain1+chain2
    print("\(concat)")
}
//Exercice 3
func weekDaysSwitch(){
    print("Enter number between 1 and 7:")
    let number = Int(readLine()!)!
    switch number {
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Satunday")
        case 7:
            print("Sunday")
        default:
            print("Bad entry...")
    }
}
func weekDaysDictionnary(){
    print("Enter number between 1 and 7:")
    let number = Int(readLine()!)!
    let days: [Int:String] = [1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Satunday",7:"Sunday"]
    let response = days[number]!
    print(response)
}
//Exercice 4
func evenOdd(){
    let tab = [4,7,5,2,13,14,16,6,11,10]
    var even = 0
    var odd = 0
    for i in 0...tab.count-1{
        if tab[i] % 2 == 0{
            even += 1
        }else{
            odd += 1
        }
    }
    print("You have \(even) even number and \(odd) odd number")
}
func positifNegatif(){
    let tab = [-4,7,5,-2,13,14,16,6,-11,10]
    var positif = 0
    var negatif = 0
    for i in 0...tab.count-1{
        if tab[i] > 0 {
            positif += 1
        }else{
            negatif += 1
        }
    }
    print("You have \(positif) positif number and \(negatif) negatif number")
}
//Exercice 5
func voyelleInChain(){
    let vayelle = "ayeoui"
    var chain = "were are you come from ?"
    var counter = 0
    chain = chain.replacingOccurrences(of:" ", with:"")
    for char in chain {
        if vayelle.contains(char) {
            counter += 1
        }
    }
    print("You have \(counter) voyelles in your sentence")
}
//Exercice 6
func ascendancyOrdered(){
    var tab = [4,7,5,2,13,14,16,6,11,10]
    var k = 0
    var tmp = 0
    for i in 0...tab.count-1{
        k = i-1
        while k>=0 && tab[k] > tab[k+1] {
            tmp = tab[k+1]
            tab[k+1] = tab[k]
            tab[k] = tmp
            k -= 1
        }
    }
    for i in 0...tab.count-1{
        print("\(tab[i])")
    }
}
func descendancyOrdered(){
    var tab = [4,7,5,2,13,14,16,6,11,10]
    var k = 0
    var tmp = 0
    for i in 0...tab.count-1{
        k = i-1
        while k>=0 && tab[k] < tab[k+1] {
            tmp = tab[k+1]
            tab[k+1] = tab[k]
            tab[k] = tmp
            k -= 1
        }
    }
    for i in 0...tab.count-1{
        print("\(tab[i])")
    }
}
//Exercice 7
func commonElement(){
    let tab1 = [4,7,5,2,13,14,16,6,11,10]
    let tab2 = [0,7,3,5,11,14,8,9,12,10]
    for i in 0...tab1.count-1{
        if tab1[i] == tab2[i] {
            print("This element: \(tab1[i])")
        }
    }
}
//Exercice 8
func tableDictionnary(){
    let dict: [Int:String] = [1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Satunday",7:"Sunday"]
    var tab1 = [String](repeating:"", count:7)
    for (cle, value) in dict{
        tab1[cle-1] = value
    }
    for i in 0...tab1.count-1{
        print("\(tab1[i])")
    }
}
//Exercice sur les boucles
//displayMessage()
//calculateMean()
//findMinimum()

/*Exercice 1*/
//exercie1()

/*Exercice 2*/
//concatChain()

/*Exercice 3*/
//weekDaysSwitch()
//weekDaysDictionnary()

/*Exercice 4*/
//evenOdd()
//positifNegatif()

/*Exercice 5*/
//voyelleInChain()

/*Exercice 6*/
//ascendancyOrdered()
//descendancyOrdered()

/*Exercice 7*/
//commonElement()

/*Exercice 8*/
//tableDictionnary()

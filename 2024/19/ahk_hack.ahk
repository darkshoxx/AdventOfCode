Text := FileRead("input.txt")
DataBlocks := StrSplit(Text, "`n")
Towels := StrSplit(DataBlocks[1], ", ")
DataBlocks.Pop()

ListToRegex(MyList) {
    StringList := []
    StringList.Push("^(")
    for index, element in MyList {
        if (index != 1) {
            StringList.Push("|")
        }
        StringList.Push("(")
        StringList.Push(element)
        StringList.Push(")")
    }
    StringList.Push(")*$")
    MyString := ""
    for index, element in StringList {
        MyString := MyString element
    }
    return MyString
}   
MyRegex := ListToRegex(Towels)

LongerString(First, Second, *) {
    return StrLen(First) - StrLen(Second)
}
SortedString := Sort(DataBlocks[1], "D ," ,LongerString)
SortedTowels := StrSplit(SortedString, ", ")
AtomicTowels := []
for index, towel in SortedTowels {
    AtomicRegex := ListToRegex(AtomicTowels)
    TowelMolecule := RegExMatch(towel, AtomicRegex)
    if (TowelMolecule == 0) {
        AtomicTowels.Push(towel)
    }
}
AtomicTowelRegex := ListToRegex(AtomicTowels)
Accumulator := 0
for index, line in DataBlocks {
    if (index > 2) {
        value := RegExMatch(line, AtomicTowelRegex)        
        Accumulator += value
    }
}
FileAppend(Accumulator, "output.txt")


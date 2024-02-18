package main

func GetCount(str string) (count int) {
	for _, char := range str {
		switch char {
		case 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U':
			count++
		}
	}
	return count
}

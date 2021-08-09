// Savesys, an easily-implementable save manager
// Written by draumaz in 2021
// BSD 3-Clause

// Example script

class main {
    public static void main(String[] args) {
        System.out.print("\nBefore conversion: " + savesys.read()[1]);
        savesys.write(1, 5);
        System.out.print("\nAfter conversion: " + savesys.read()[1]);
    }
}

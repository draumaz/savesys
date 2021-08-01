// Savesys, an easily-implementable save manager
// Written by draumaz in 2021
// BSD 3-Clause

// Example script

class main {
    public static void main(String[] args) {
        savesys sv = new savesys();
        System.out.print("\nBefore conversion: " + sv.read()[1]);
        sv.write(1, 5);
        System.out.print("\nAfter conversion: " + sv.read()[1]);
    }
}

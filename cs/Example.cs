// Savesys, an easily-implementable save manager
// Written by draumaz in 2021
// BSD 3-Clause

using Savesys;

namespace Example
{
    public class Program
    {
        public static void Main()
        {
            Savesys.IO.Save_Gen();
            int[] before = Savesys.IO.Save_Read();
            int be4 = before[1];
            Console.WriteLine("Before conversion {0}", be4);
            int line = 1; // Assign line to '1' (line 2)
            int state = 5; // Assign state to '2'
            Savesys.IO.Save_Write(line, state); // Write
            int[] after = Savesys.IO.Save_Read();
            int a4tr = after[1];
            Console.WriteLine("After conversion {0}", a4tr);
        }
    }
}

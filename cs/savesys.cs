// Non-functional, still in development //

using System;
using System.IO;
using System.Linq;

namespace Savesys
{
    public class IO
    {
        public static int[] Save_Read()
        {
            string[] x = File.ReadAllLines("data.txt");
            int[] y = Array.ConvertAll(x, int.Parse);
            return y;
        }
        public static void Save_Write(int line, int state)
        {
            int[] write_array = Save_Read();
            write_array[line] = state;
        }
        public static void Save_Gen()
        {
            File.WriteAllText("data.txt", "0\n0\n0\n0\n0\n");
        }
    }
}

namespace Test
{
    public class Toest
    {
        public static void Main()
        {
            int[] i = Savesys.IO.Save_Read();
        }
    }
}

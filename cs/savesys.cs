// Savesys, an easily-implementable save manager
// Written by draumaz in 2021
// BSD 3-Clause

using System;
using System.IO;
using System.Linq;

namespace Savesys
{
    class Path_Settings
    {
        public static string Paths(int m)
        {
            string save_path = "data.txt"; // Customize here!
            string save_len = "0\n0\n0\n0\n0";
            if (m == 1)
            {
                return save_path;
            }
            if (m == 2)
            {
                return save_len;
            }
            return "Error";
        }
    }
    public class IO
    {
        public static int[] Save_Read()
        {
            int m = 1; // Path set
            string[] x = File.ReadAllLines(Path_Settings.Paths(m)); // Write file lines to string array
            int[] y = Array.ConvertAll(x, int.Parse); // Convert to int array
            return y; // Return int array
        }
        public static void Save_Write(int line, int state) // line - line number from 0; state - variable to insert
        {
            int m = 1; // Path Set
            int[] read_array = Save_Read(); // Fetch variables into array
            read_array[line] = state; // Director
            string[] write_array = read_array.Select(x => x.ToString()).ToArray(); // Convert to string array
            File.WriteAllLines(Path_Settings.Paths(m), write_array); // Write to file
        }
        public static void Save_Gen()
        {
            int m = 1; // Path Set
            int mm = 2; // Path Set
            string sl = Path_Settings.Paths(m);
            string sp = Path_Settings.Paths(mm);
            File.WriteAllText(sl, sp); // Write to file
        }
    }
}

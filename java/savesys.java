// Savesys, an easily-implementable save manager
// Written by draumaz in 2021
// BSD 3-Clause

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

class savesys {
    public static String save_name() {
        return "temp.txt"; // default filename {CONFIG}
    }
    public static int save_default() {
        return 10; // default line variables {CONFIG}
    }
    public static void exists() {
        if (new File(save_name()).exists());
        else
            generate();
    }
    public static int generate() {
        try {
                new File(save_name()).createNewFile(); // generate file
            } catch (IOException I) {
                return 1; 
            }
            try {
                BufferedWriter buf = null;
                buf = new BufferedWriter(new FileWriter(save_name())); // open writer
                for (int fr = 0; fr < save_default(); fr++) { 
                    buf.write(0+"\n"); // loop write save_default() variables
                }
                buf.flush();
                buf.close();
            } catch (IOException io) {
                return 1;
            }
            return 0;
    }
    public static int[] read() {
		int[] wr = new int[save_default()]; // set array size
		try {
			List<String> z = Files.readAllLines(Paths.get(save_name())); // pull into list
			String[] str_arr = z.stream().toArray(String[]::new); // convert to string array
			for (int fr = 0; fr < wr.length; fr++) {
				wr[fr] = Integer.parseInt(str_arr[fr]); // loop convert into int array
			}
		} catch (IOException io) {}
		  catch (ArrayIndexOutOfBoundsException a) {
		  	generate();
			System.out.println("\nSave corrupted. Continuing with a new save.");
		}
		return wr;
	}
    public static int write(int line, int state) {
		int[] r = read(); // get current save
		try {
			BufferedWriter buf = null;
			buf = new BufferedWriter(new FileWriter(save_name())); // initalize writer
			for (int i = 0; i < r.length; i++) {
                if (i == line) {
                    buf.write(Math.round((int)(state < 0? 0 : state))+"\n"); // write requested state to line
                    continue;
                }
				buf.write(r[i]+"\n"); // loop write to file
			}
			buf.flush();
			buf.close();
		} catch (IOException io) {
            return 1;
        }
        return 0;
    }
}

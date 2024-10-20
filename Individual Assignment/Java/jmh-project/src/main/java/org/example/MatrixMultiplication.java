package org.example;

import java.util.Random;

public class MatrixMultiplication {

	public double[][] execute(int n) {
		double[][] a = new double[n][n];
		double[][] b = new double[n][n];
		Random random = new Random();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				a[i][j] = random.nextDouble();
				b[i][j] = random.nextDouble();
			}
		}
		double[][] c = new double[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					c[i][j] += a[i][k] * b[k][j];
				}
			}
		}
		return c;
	}
}

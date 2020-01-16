﻿// Auto-Focus-Cpp.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <string>
#include <vector>
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2\imgproc\imgproc.hpp>
#include <opencv2\imgproc\imgproc_c.h>
#include <opencv2\highgui\highgui.hpp>

using namespace cv;
using namespace std;

//Calculate length of array
//overloaded function 1: pointer array of int type
int ArrayLength(int* which_array) {

	int length = _msize(which_array) / sizeof(which_array[0]);

	return length;
}
//overloaded function 2: pointer array of float type
int ArrayLength(float* which_array) {

	int length = _msize(which_array) / sizeof(which_array[0]);

	return length;
}
//overloaded function 3: array pointer of double type
int ArrayLength(double* which_array) {

	int length = _msize(which_array) / sizeof(which_array[0]);

	return length;
}
//overloaded function 4: pointer array of char type
//char could be the pointer variable
int ArrayLength(char* which_array) {

	int length = _msize(which_array) / sizeof(which_array[0]);

	return length;
}

//Calculate sum of array
//overloaded function 1: pointer array of int type
int ArraySum(int* which_array) {

	//final result
	int sum = 0;

	for (int i = 0; i < ArrayLength(which_array); i++) {

		sum += which_array[i];
	}
	return sum;
}
//overloaded function 2: pointer array of float type
float ArraySum(float* which_array) {

	//final result
	float sum = 0;

	for (int i = 0; i < ArrayLength(which_array); i++) {

		sum += which_array[i];
	}
	return sum;
}
//overloaded function 3: pointer array of double type
double ArraySum(double* which_array) {

	//final result
	double sum = 0;

	for (int i = 0; i < ArrayLength(which_array); i++) {

		sum += which_array[i];
	}
	return sum;
}

//Calculate sum of vector
//overloaded function 1: vector of int type
int VectorSum(vector<int> which_vector) {

	//final result
	int sum = 0;

	for (int i = 0; i < which_vector.size(); i++) {
	
		sum += which_vector[i];
	}
	return sum;
}
//overloaded function 2: vector of float type
float VectorSum(vector<float> which_vector) {

	//final result
	float sum = 0;

	for (int i = 0; i < which_vector.size(); i++) {

		sum += which_vector[i];
	}
	return sum;
}
//overloaded function 3: vector of double type
double VectorSum(vector<double> which_vector) {

	//final result
	double sum = 0;

	for (int i = 0; i < which_vector.size(); i++) {

		sum += which_vector[i];
	}
	return sum;
}

//Calculate average of array
//overloaded function 1: pointer array of int type
double ArrayAverage(int* which_array) {

	int sum = ArraySum(which_array);

	return double(sum) / ArrayLength(which_array);
}
//overloaded function 1: pointer array of float type
double ArrayAverage(float* which_array) {

	float sum = ArraySum(which_array);

	return double(sum) / ArrayLength(which_array);
}
//overloaded function 1: pointer array of double type
double ArrayAverage(double* which_array) {

	double sum = ArraySum(which_array);

	return double(sum) / ArrayLength(which_array);
}

//Calculate average of vector
//overloaded function 1: vector of int type
double VectorAverage(vector<int> which_vector) {

	int sum = VectorSum(which_vector);

	return double(sum) / which_vector.size();
}
//overloaded function 2: vector of float type
double VectorAverage(vector<float> which_vector) {

	float sum = VectorSum(which_vector);

	return double(sum) / which_vector.size();
}
//overloaded function 2: vector of double type
double VectorAverage(vector<double> which_vector) {

	double sum = VectorSum(which_vector);

	return double(sum) / which_vector.size();
}

//Calculate maximum in an vector
//overloaded function 1: vector of int type
int VectorMaximum(vector<int> which_vector) {

	//init the maximum
	int maximum = which_vector[0];

	for (int i = 0; i < which_vector.size(); i++) {

		if (which_vector[i] > maximum) {

			maximum = which_vector[i];
		}
	}
	return maximum;
}
//overloaded function 2: vector of double type
double VectorMaximum(vector<double> which_vector) {

	//init the maximum
	double maximum = which_vector[0];

	for (int i = 0; i < which_vector.size(); i++) {

		if (which_vector[i] > maximum) {

			maximum = which_vector[i];
		}
	}
	return maximum;
}

//Calculate minimum in an vector
//overloaded function 1: vector of int type
int VectorMinimum(vector<int> which_vector) {

	//init the minimum
	int minimum = which_vector[0];

	for (int i = 0; i < which_vector.size(); i++) {

		if (which_vector[i] < minimum) {

			minimum = which_vector[i];
		}
	}
	return minimum;
}
//overloaded function 2: vector of double type
int VectorMinimum(vector<double> which_vector) {

	//init the minimum
	double minimum = which_vector[0];

	for (int i = 0; i < which_vector.size(); i++) {

		if (which_vector[i] < minimum) {

			minimum = which_vector[i];
		}
	}
	return minimum;
}

//The array elements are multiplied
//overloaded function 1: both array of int
int ArrayMultiplication(int* array_A, int* array_B) {

	//judge if the length is the same
	if (ArrayLength(array_A) == ArrayLength(array_B)) {

		//final result
		int sum = 0;

		for (int i = 0; i < ArrayLength(array_A); i++) {
		
			sum += array_A[i] * array_B[i];
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of array";
		return 0;
	}
}
//overloaded function 2: array of int and float
float ArrayMultiplication(int* array_A, float* array_B) {

	//judge if the length is the same
	if (ArrayLength(array_A) == ArrayLength(array_B)) {

		//final result
		float sum = 0;

		for (int i = 0; i < ArrayLength(array_A); i++) {

			sum += array_A[i] * array_B[i];
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of array";
		return 0;
	}
}
//overloaded function 3: array of int and double
double ArrayMultiplication(int* array_A, double* array_B) {

	//judge if the length is the same
	if (ArrayLength(array_A) == ArrayLength(array_B)) {

		//final result
		double sum = 0;

		for (int i = 0; i < ArrayLength(array_A); i++) {

			sum += array_A[i] * array_B[i];
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of array";
		return 0;
	}
}

//The vector elements are multiplied
//overloaded function 1: both array of int
int VectorMultiplication(vector<int> vector_A, vector<int> vector_B) {

	//judge if the length is the same
	if (vector_A.size() == vector_B.size()) {

		//final result
		int sum = 0;

		for (int i = 0; i < vector_A.size(); i++) {

			sum += vector_A[i] * vector_B[i];
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of vector";
		return 0;
	}
}
//overloaded function 2: both array of double
int VectorMultiplication(vector<double> vector_A, vector<double> vector_B) {

	//judge if the length is the same
	if (vector_A.size() == vector_B.size()) {

		//final result
		double sum = 0;

		for (int i = 0; i < vector_A.size(); i++) {

			sum += vector_A[i] * vector_B[i];
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of vector";
		return 0;
	}
}
//overloaded function 3: vector of int and double
int VectorMultiplication(vector<int> vector_A, vector<double> vector_B) {

	//judge if the length is the same
	if (vector_A.size() == vector_B.size()) {

		//final result
		double sum = 0;

		for (int i = 0; i < vector_A.size(); i++) {

			sum += double(vector_A[i]) * vector_B[i];
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of vector";
		return 0;
	}
}
int VectorMultiplication(vector<double> vector_A, vector<int> vector_B) {

	//judge if the length is the same
	if (vector_A.size() == vector_B.size()) {

		//final result
		double sum = 0;

		for (int i = 0; i < vector_A.size(); i++) {

			sum += vector_A[i] * double(vector_B[i]);
		}
		return sum;
	}
	else {

		cout << "--> ERROR: Incorrct size of vector";
		return 0;
	}
}

//list of index of value which is bigger than threshold which_array
//overloaded function 1: pointer array of int type
vector<int> VectorIndexAboveThreshold(int* which_array, double threshold) {

	const int length = ArrayLength(which_array);

	//final result
	vector <int> list_index;

	for (int i = 0; i < length; i++) {

		if (which_array[i] > threshold) {

			list_index.push_back(i);
		}
	}
	return list_index;
}
//overloaded function 2: vector of int type
vector<int> VectorIndexAboveThreshold(vector<int> which_array, double threshold) {

	//final result
	vector <int> list_index;

	for (int i = 0; i < which_array.size(); i++) {

		if (which_array[i] > threshold) {

			list_index.push_back(i);
		}
	}
	return list_index;
}

//list of index of value which is smaller than threshold which_array
vector<int> VectorIndexBelowThreshold(int* which_array, double threshold) {

	const int length = ArrayLength(which_array);

	//final result
	vector <int> list_index;

	for (int i = 0; i < length; i++) {

		if (which_array[i] < threshold) {

			list_index.push_back(i);
		}
	}
	return list_index;
}
//overloaded function 2: vector of int type
vector<int> VectorIndexBelowThreshold(vector<int> which_array, double threshold) {

	//final result
	vector <int> list_index;

	for (int i = 0; i < which_array.size(); i++) {

		if (which_array[i] < threshold) {

			list_index.push_back(i);
		}
	}
	return list_index;
}

//Calculate ROI matrix as an vector
vector<int> VectorROI(Mat img_gray, int center_ROI[2]) {

	//size of matrix
	int height = img_gray.rows;
	int width = img_gray.cols;

	//5-Area ROI size
	int height_ROI = int(height / 9);
	int width_ROI = int(width / 9);

	//half size
	int half_height_ROI = int(height / 18);
	int half_width_ROI = int(width / 18);

	//amount of pixel in ROI
	int area_ROI = height_ROI * width_ROI;

	//ROI matrix
	vector<int> ROI;

	//give value to ROI matrix object
	int i;
	int j;
	int i_start = center_ROI[0] - half_height_ROI;
	int j_start = center_ROI[1] - half_width_ROI;

	for (i = 0; i < height_ROI; i++) {

		for (j = 0; j < width_ROI; j++) {

			ROI.push_back(img_gray.ptr<uchar>(i_start + i)[j_start + j]);

		}
	}
	//judge whether it is correct
	//cout << ROI.size() << endl;
	//cout << ROI[0] << endl;
	return ROI;
}

//Flatten img matrix as a vector
vector <int> VectorImgGray(Mat img_gray) {

	//size of img
	int height = img_gray.rows;
	int width = img_gray.cols;

	//matrix as an array
	vector<int> vector_img_gray;

	//get the number of pixels under each gray level is obtained
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			vector_img_gray.push_back(img_gray.at<uchar>(i, j));
		}
	}
	return vector_img_gray;
}

//Calculate gray level
vector<int> VectorGrayLevel(int step_gray_level) {

	//gray level vector
	vector<int>gray_level;

	//give value
	for (int i = 0; i < int(256/ step_gray_level); i++) {

		gray_level.push_back(i);
	}
	return gray_level;
}

//Calculate ROI matrix gray level amount vector
vector<int> VectorGrayLevelAmount(vector<int> vector_img_gray) {

	//gray level amount vector
	vector<int>amount;

	//init
	for (int i = 0; i < 256; i++) {

		amount.push_back(0);
	}

	//accumulate
	for (int k = 0; k < vector_img_gray.size(); k++) {
		
		amount[int(vector_img_gray[k])]++;
	}
	return amount;
}

//Calculate ROI matrix gray level frequency vector
vector<double> VectorGrayLevelFrequency(vector<int> vector_img_gray) {

	//ROI matrix gray level amount
	vector<int>amount = VectorGrayLevelAmount(vector_img_gray);

	//ROI matrix gray level frequency vector
	vector<double>frequency;

	//the probability distribution of each gray level is obtained
	for (int i = 0; i < amount.size(); i++) {

		frequency.push_back((double)amount[i] / vector_img_gray.size());
	}
	return frequency;
}

//Calculate contrast of ROI vector
double CalculateContrast(vector<int> vector_ROI, const string contrast_operator) {

	//maximum and minimum of ROI vector
	int L_maximum = VectorMaximum(vector_ROI);
	int L_minimum = VectorMinimum(vector_ROI);

	//convert to double (+0.5 to avoid overflow)
	double L_max = static_cast<double>(L_maximum) + 0.5;
	double L_min = static_cast<double>(L_minimum) + 0.5;

	//final result
	double contrast;

	//Michelson (1927)
	if (contrast_operator == "Michelson") {

		contrast = (L_max - L_min) / (L_max + L_min);

	}
	//Whittle (1986)
	if (contrast_operator == "Whittle") {

		contrast = (L_max - L_min) / (L_min);

	}
	//Weber (1840)
	if (contrast_operator == "Weber") {

		contrast = L_max - L_min;

	}
	//W3C (2006)
	if (contrast_operator == "W3C") {

		contrast = (L_max + 0.05) / (L_min + 0.05);

	}
	//Boccignone (1996)
	if (contrast_operator == "Boccignone") {

		contrast = L_max - L_min;

	}
	//Moulden (1990): Standard Deviation
	//judge if 'S' is in the string
	if ((contrast_operator.find("S") != string::npos)) {

		cout << contrast_operator << endl;
	}
	
	//SD: standard deviation
	if (contrast_operator == "SD") {

		contrast = L_max - L_min;

	}
	//SDLG: standard deviation of logarithm of luminance
	if (contrast_operator == "SDLG") {

		contrast = L_max - L_min;

	}
	//SAW: space-average of Whittle contrast
	if (contrast_operator == "SAW") {

		contrast = L_max - L_min;

	}
	return contrast;
}
int main()
{
	cout << "Built with OpenCV " << CV_VERSION << endl;
	Mat img_bgr= imread("bar.jpg", 1);

	if (!img_bgr.data)  //or == if(src.empty())
	{
		cout << "Could not open or find the image" << endl;
		return -1;
	}

	//size of img
	int height = img_bgr.rows;
	int width = img_bgr.cols;

	//cout << height << endl;
	//cout << width << endl;

	//construct img gray//
	Mat img_gray(height, width, CV_8UC1);
	cvtColor(img_bgr, img_gray, CV_BGR2GRAY);

	//5-Area ROI center
	int center_ROI_A[2] = { int(height / 2) ,int(height / 2) };
	int center_ROI_B[2] = { int(height / 4) ,int(height / 4) };
	int center_ROI_C[2] = { int(height / 4) ,int(3 * height / 4) };
	int center_ROI_D[2] = { int(3 * height / 4) ,int(height / 4) };
	int center_ROI_E[2] = { int(3 * height / 4) ,int(3 * height / 4) };

	//5-Area ROI vector
	vector <int>ROI_A = VectorROI(img_gray, center_ROI_A);
	vector <int>ROI_B = VectorROI(img_gray, center_ROI_B);
	vector <int>ROI_C = VectorROI(img_gray, center_ROI_C);
	vector <int>ROI_D = VectorROI(img_gray, center_ROI_D);
	vector <int>ROI_E = VectorROI(img_gray, center_ROI_E);

	vector <int>gray_level = VectorGrayLevel(1);
	vector <double>gray_frequency = VectorGrayLevelFrequency(ROI_A);

	//calculate avearge gray level
	double L_mean = VectorMultiplication(gray_level, gray_frequency);

	//calculate index of gray value who is smaller or bigger than threshold
	vector <int> index_list_below_threshold = VectorIndexBelowThreshold(gray_level, L_mean);
	vector <int> index_list_above_threshold = VectorIndexAboveThreshold(gray_level, L_mean);
	
	//cout << index_list_below_threshold.size() << endl;
	//cout << index_list_above_threshold.size() << endl;

	//double contrast = CalculateContrast(ROI, "Michelson");
	//double contrast = CalculateContrast(ROI, "Whittle");
	double contrast = CalculateContrast(ROI_A, "SD");

	cout << contrast << endl;

	//delete corresponds to new and delete[] corresponds to new[]
	//delete and delete[] play the same role in built-in data structure (pointer variable)
}

// -*- coding: utf-8 -*-
/******************************************************************************
Created on Mon Sept 11 14:51:37 2020

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: wei@kamerawerk.cn

@title: script-Automatic Focusing Simulation
******************************************************************************/

// main.cpp: This file contains the "main" function.
// This is where program execution begins and ends

#include "init.h"

#include "Header\object_frame.h"

#include "Header\operation_import.h"
#include "Header\operation_vector.h"

#include "Header\calculation_contrast.h"
#include "Header\calculation_peak_search.h"
#include "Header\calculation_numerical_analysis.h"

int main(){

	cout << "Built with OpenCV " << CV_VERSION << endl;

	//Mat img_QR_code = ReadImgBGR("AF_QR_Code_Scanner.jpg");
	//ReadQRCode(img_QR_code, "zxing-cpp-master");

	string imgs_path = "E:/GitHub/KAMERAWERK/VCM-Dual/Material/Stereo Effect Experiment/g=666mm/Left";

	Mat image = imread(imgs_path + "/VCM_420.jpg");
	Mat gray;
	cvtColor(image, gray, COLOR_BGR2GRAY);

	//write gray value
	ofstream gray_file;
	gray_file.open("../Outcome/gray-off-line.txt");

	int sum;
	for (int i = 0; i < gray.rows; ++i) {
		sum = 0;
		for (int j = 0; j < gray.cols; ++j) {

			//cout << "[" << i << ", " << j << "]" << endl;
			//cout << int(image.at<Vec3b>(i, j)[0]) << ", " << int(image.at<Vec3b>(i, j)[1]) << ", " << int(image.at<Vec3b>(i, j)[2]) << endl;

			sum += int(gray.at<uchar>(i, j));
			gray_file << int(gray.at<uchar>(i, j)) << " ";
		}
		//cout << sum << endl;
		gray_file << endl;
	}
	/*cout << image.size() << endl;
	cout << int(image.at<Vec3b>(100, 100)[0]) << endl;
	cout << int(image.at<Vec3b>(100, 100)[1]) << endl;
	cout << int(image.at<Vec3b>(100, 100)[2]) << endl;*/

	//namedWindow("g", WINDOW_NORMAL);

	//resizeWindow("g", 800, 600);
	//imshow("g", gray);
	//
	//waitKey(0);

	vector<frame> vector_frame = VectorFrame(imgs_path);
	
	//vector of code and contrast
	vector<int> vector_code;
	vector<double> vector_contrast;

	for (int k = 0; k < vector_frame.size(); k++) {

		vector_code.push_back(vector_frame[k].lens_position_code);
		vector_contrast.push_back(vector_frame[k].focus_value);

		GlobalSearch(vector_contrast);
	}
	//write VCM Code and contrast
	ofstream out_file;
	out_file.open("../Outcome/Code-Contrast.txt");
	out_file << "Code" << " " << "Contrast" << endl;

	//normalization
	vector<double> vector_normalized_contrast = Normalize(vector_contrast);

	for (int k = 0; k < vector_contrast.size(); k++) {

		cout << "--> Code: " << vector_code[k] << ", Value: " << vector_contrast[k] << endl;
		out_file << vector_code[k] << " " << vector_normalized_contrast[k] << endl;
	}
	
	int focused_code = vector_frame[GlobalSearch(vector_contrast)].lens_position_code;
	cout << endl << "--> Focused Lens Position Code: " << focused_code << endl;
	
	return 0;

	//plot the curve

	//delete corresponds to new and delete[] corresponds to new[]
	//delete and delete[] play the same role in built-in data structure (pointer variable)
}
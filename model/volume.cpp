#pragma warning ( disable : 4786 )

#include "itkImageLinearConstIteratorWithIndex.h"
#include "itkImageLinearIteratorWithIndex.h"
#include "itkImage.h"

#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"

#include <iostream>
using namespace std;

int main(int argc,char* argv[]) {
	
	if(argc<2) {
		std::cerr << "debe especificar un nombre de fichero" << std::endl;
		return -1;
	}


	typedef unsigned char       PixelType;
	const unsigned int          Dimension = 3;

	typedef itk::Image<PixelType, Dimension > ImageType;

	typedef itk::ImageFileReader< ImageType > ReaderType;
	ReaderType::Pointer reader = ReaderType::New();
	reader->SetFileName( argv[1] );

	try	{
		reader->Update();
	}
	catch( itk::ExceptionObject & excp ) {
		std::cerr << "Problem reading image file : " << argv[1] << std::endl;
		std::cerr << excp << std::endl;
		return -1;
	}

	ImageType::Pointer inputImage = reader->GetOutput();

	typedef itk::ImageLinearConstIteratorWithIndex< ImageType >  ConstIteratorType;
		
	ConstIteratorType inputIt( inputImage, inputImage->GetRequestedRegion() );
	inputIt.SetDirection(0);
	
	ImageType::IndexType start_idx0, end_idx0, max_start_idx0, max_end_idx0;
	int len0, maxLen0, vol = 0;
	maxLen0 = 0;

	char a[1000];
	for(inputIt.GoToBegin(); ! inputIt.IsAtEnd(); inputIt.NextLine()) {
			inputIt.GoToBeginOfLine();
			len0 = 0;
			//std::cout << "Una iteracion" << std::endl;
			//std::cout << vol << std::endl; //Volumen count
			//std::cout << maxLen0 << std::endl; //Max len X
			//std::cout << max_start_idx0 << std::endl; //Start index X
			//std::cout << max_end_idx0 << std::endl; //End index X 
			//std::cin >> a;
			while ( ! inputIt.IsAtEndOfLine() ) {
				if(inputIt.Get() == 255) {
					vol++;
					if(len0==0)
						start_idx0 = inputIt.GetIndex();
					len0++;
				} else {
					if(maxLen0 < len0) {
						maxLen0 = len0;
						len0 = 0;
						max_start_idx0 = start_idx0;
						max_end_idx0 = inputIt.GetIndex();
					}
				}
				++inputIt;
			}
			if(maxLen0 < len0 && inputIt.IsAtEndOfLine()) {
				maxLen0 = len0;
				len0 = 0;
				max_start_idx0 = start_idx0;
				max_end_idx0 = inputIt.GetIndex();
			}
	}
	
	
	inputIt.SetDirection(1);
	ImageType::IndexType start_idx1, end_idx1, max_start_idx1, max_end_idx1;
	int len1, maxLen1;
	maxLen1 = 0;
	
	for(inputIt.GoToBegin(); ! inputIt.IsAtEnd(); inputIt.NextLine()) {
			inputIt.GoToBeginOfLine();
			len1 = 0;
			while ( ! inputIt.IsAtEndOfLine() ) {
				if(inputIt.Get() == 255) {
					if(len1==0)
						start_idx1 = inputIt.GetIndex();
					len1++;
				} else {
					if(maxLen1 < len1) {
						maxLen1 = len1;
						len1 = 0;
						max_start_idx1 = start_idx1;
						max_end_idx1 = inputIt.GetIndex();
					}
				}
				++inputIt;
			}
			if(maxLen1 < len1 && inputIt.IsAtEndOfLine()) {
				maxLen1 = len1;
				len1 = 0;
				max_start_idx1 = start_idx1;
				max_end_idx1 = inputIt.GetIndex();
			}
	}

	
	inputIt.SetDirection(2);
	ImageType::IndexType start_idx2, end_idx2, max_start_idx2, max_end_idx2;
	int len2, maxLen2;
	maxLen2 = 0;
	
	for(inputIt.GoToBegin(); ! inputIt.IsAtEnd(); inputIt.NextLine()) {
			inputIt.GoToBeginOfLine();
			len2 = 0;
			while ( ! inputIt.IsAtEndOfLine() ) {
				if(inputIt.Get() == 255) {
					if(len2==0)
						start_idx2 = inputIt.GetIndex();
					len2++;
				} else {
					if(maxLen2 < len2) {
						maxLen2 = len2;
						len2 = 0;
						max_start_idx2 = start_idx2;
						max_end_idx2 = inputIt.GetIndex();
					}
				}
				++inputIt;
			}
			if(maxLen2 < len2 && inputIt.IsAtEndOfLine()) {
				maxLen2 = len2;
				len2 = 0;
				max_start_idx2 = start_idx2;
				max_end_idx2 = inputIt.GetIndex();
			}
	}

	if(argc==2) {
		cout << vol << std::endl; //Volumen count
		cout << maxLen0 << std::endl; //Max len X
		cout << max_start_idx0 << std::endl; //Start index X
		cout << max_end_idx0 << std::endl; //End index X 
		cout << maxLen1 << std::endl; //Max len Y
		cout << max_start_idx1 << std::endl; //Start index Y
		cout << max_end_idx1 << std::endl; //End index Y
		cout << maxLen2 << std::endl; //Max len Z
		cout << max_start_idx2 << std::endl; //Start index Z
		cout << max_end_idx2 << std::endl; //End index Z
	} 
	if(argc==3) {
		FILE *f = fopen(argv[2],"wt");
		fprintf(f,"%d\n",vol); //Volumen count
		fprintf(f,"%d\n",maxLen0); //Max len X
		fprintf(f,"[%d, %d, %d]\n",max_start_idx0[0],max_start_idx0[1],max_start_idx0[2]); //Start index X
		fprintf(f,"[%d, %d, %d]\n",max_end_idx0[0],max_end_idx0[1],max_end_idx0[2]); //End index X 
		fprintf(f,"%d\n",maxLen1); //Max len Y
		fprintf(f,"[%d, %d, %d]\n",max_start_idx1[0],max_start_idx1[1],max_start_idx1[2]); //Start index X
		fprintf(f,"[%d, %d, %d]\n",max_end_idx1[0],max_end_idx1[1],max_end_idx1[2]); //End index X 
		fprintf(f,"%d\n",maxLen2); //Max len Z
		fprintf(f,"[%d, %d, %d]\n",max_start_idx2[0],max_start_idx2[1],max_start_idx2[2]); //Start index X
		fprintf(f,"[%d, %d, %d]\n",max_end_idx2[0],max_end_idx2[1],max_end_idx2[2]); //End index X 
		fclose(f);
	}
	return 0;
  
}
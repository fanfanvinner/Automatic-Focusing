/////////////////////////////////////////////////////////////
// All Rights Reserved by DOTHINKEY
// Last Update:2010 01 20
/////////////////////////////////////////////////////////////

#include "StdAfx.h"
#include "IniFileRW.h"
#include "../DTCCM2_SDK/imagekit.h"
#include "diskinfo.h"

CString m_sIniFile="";
int m_nIniCurDev = 0;

//////////////////////////////////////////////////////////////////////////
//��õ�ǰexe·��������ֵ������·��
//
//
//////////////////////////////////////////////////////////////////////////
CString sIniPathName()
{
	TCHAR sFilename[_MAX_PATH];
	TCHAR sDrive[_MAX_DRIVE];
	TCHAR sDir[_MAX_DIR];
	TCHAR sFname[_MAX_FNAME];
	TCHAR sExt[_MAX_EXT];
	GetModuleFileName(AfxGetInstanceHandle(), sFilename, _MAX_PATH);
	_tsplitpath_s(sFilename, sDrive, sDir, sFname, sExt);

	CString rVal(CString(sDrive) + CString(sDir));
	
	if ( rVal.Right(1) != _T('\\') )
		rVal += _T("\\"); 

	return rVal;
}

//////////////////////////////////////////////////////////////////////////
//���ص�ǰini�ļ�������������ڣ�����Ĭ�ϵ�hsset.ini�ļ�
//////////////////////////////////////////////////////////////////////////
CString sIniFileName()
{
	if(m_sIniFile.IsEmpty())
	{
		if(m_nIniCurDev <= 0)
			m_sIniFile.Format("%shsset.ini", sIniPathName());
		else
			m_sIniFile.Format("%shsset_%d.ini", sIniPathName(),m_nIniCurDev + 1);
		//AfxMessageBox(m_sIniFile);
	}
	
    return m_sIniFile;
}

//////////////////////////////////////////////////////////////////////////
//���õ�ǰini�ļ�������·����Ҳ����ini�ļ�һ���ǵ�ǰexe����·������
//
//////////////////////////////////////////////////////////////////////////
void SetIniFileNameInExePath(CString sFileName)
{
	m_sIniFile = sIniPathName() + sFileName;
}

//////////////////////////////////////////////////////////////////////////
//���ð���·����ini�ļ�����sFileName���뺬��·����
//
//////////////////////////////////////////////////////////////////////////
void SetIniFileName(CString sFileName)
{
	m_sIniFile = sFileName;
}

//////////////////////////////////////////////////////////////////////////
//��ǰ�ļ������
//////////////////////////////////////////////////////////////////////////
//
void ClearIniFileName()
{
	m_sIniFile.Empty();
}

//////////////////////////////////////////////////////////////////////////
//д���ݵ�ini�ļ�
//////////////////////////////////////////////////////////////////////////
BOOL WriteIniData(CString sSection, CString sSectionKey, int nValue)
{
	CString  sValue;
	sValue.Format("%d",nValue);
	return WritePrivateProfileString(sSection,sSectionKey,sValue,sIniFileName());
}

//////////////////////////////////////////////////////////////////////////
//��ini�ļ�������
//////////////////////////////////////////////////////////////////////////
int ReadIniData(CString sSection,CString sSectionKey,int nDefault)
{
    return GetPrivateProfileInt(sSection,sSectionKey,nDefault,sIniFileName());
}

//////////////////////////////////////////////////////////////////////////
//д�ַ�����ini�ļ�
//////////////////////////////////////////////////////////////////////////
BOOL WriteIniString(CString sSection, CString sSectionKey, CString sValue)
{
	return WritePrivateProfileString(sSection,sSectionKey,sValue,sIniFileName());
}

//////////////////////////////////////////////////////////////////////////
//��ini�ļ����ַ���
//////////////////////////////////////////////////////////////////////////
CString ReadIniString(CString sSection,CString sSectionKey,CString sDefault)
{
	CString sTemp;
	GetPrivateProfileString(sSection, sSectionKey, sDefault, sTemp.GetBuffer(MAX_PATH), MAX_PATH, sIniFileName());
	sTemp.TrimLeft();
	sTemp.TrimRight();
	sTemp.ReleaseBuffer();
	return sTemp;
}

//////////////////////////////////////////////////////////////////////////
//��ini�ļ���ʮ����������
//////////////////////////////////////////////////////////////////////////
long ReadIniDataHex(CString sSection,CString sSectionKey,long nDefault)
{
    CString sTemp;
	GetPrivateProfileString(sSection,sSectionKey,"", sTemp.GetBuffer(MAX_PATH), MAX_PATH, sIniFileName());
	sTemp.ReleaseBuffer();
	char* pAddr = sTemp.GetBuffer(MAX_PATH); 
	long x = sTemp.IsEmpty() ? nDefault : strtoul( pAddr, NULL, 16); 
	sTemp.ReleaseBuffer();
	return x;
}

//////////////////////////////////////////////////////////////////////////
//дʮ���������ݵ��ļ�
//////////////////////////////////////////////////////////////////////////
BOOL WriteIniDataHex(CString sSection, CString sSectionKey, long nValue)
{
	CString sTmp;
	sTmp.Format("%x", nValue);
	return WritePrivateProfileString(sSection, sSectionKey, sTmp, sIniFileName());
}

UINT GetParaFromFile(CString sFile, CString sSection, UINT *pBuf)
{
	CStdioFile file;
	if (!file.Open((sFile), CFile::modeRead | CFile::typeText))
	{
		return FALSE;
	}
	CString szLine = _T(" ");
	CString sReg, sVal;
	UINT reg, value;
	int tmp = 0;
	BOOL bRet = 0;

	sSection.MakeLower();
	sSection.TrimLeft();
	sSection.TrimRight();	

	UINT* pData = pBuf;
	UINT ParaListSize = 0;
	BOOL bStart = 0;
	ULONGLONG fileLen = file.GetLength();
	while(1)
	{
		if(fileLen < file.GetPosition())
		{
			break;
		}

		bRet = file.ReadString(szLine);
		if(!bRet)
		{
			break;
		}

		//Ѱ��ע�ͷ��Ż���']',����������ģ�ֻȡǰ��ģ�
		tmp = szLine.FindOneOf("//"); 
		if( tmp == 0)
		{
			continue;
		}
		else if(tmp > 0)
		{
			szLine = szLine.Left(tmp);
		}
		tmp = szLine.FindOneOf("]"); 
		if( tmp == 0)
		{
			continue;
		}
		else if(tmp > 0)
		{
			szLine = szLine.Left(tmp+1);
		}
		szLine.MakeLower();
		szLine.TrimLeft();
		szLine.TrimRight();		

		if(!bStart)
		{
			if(strcmp(szLine, sSection)) 
			{
				continue;
			}
			bStart =  1;
			continue;
		}

		if(szLine.IsEmpty())
			continue;
		else if(szLine.Left(1) == ",")
			continue;
		else if(szLine.Left(1) == ";")
			continue;
		else if(szLine.Left(1) == "/")
			continue;

		else if(szLine.Left(1) == "[")
		{
			break;
		}
		//	AfxMessageBox(szLine);
		AfxExtractSubString(sReg, szLine, 0, ',');
		AfxExtractSubString(sVal, szLine, 1, ',');
		sReg.TrimLeft();   
		sReg.TrimRight();
		sVal.TrimLeft();
		sVal.TrimRight();  

		if(!sscanf_s(sReg, "0x%x", &reg)) //��ȡ��ֵ������	
			sscanf_s(sReg, "%d", &reg);

		if(!sscanf_s(sVal, "0x%x", &value)) //��ȡ��ֵ������	
			sscanf_s(sVal, "%d", &value);

		*pData = reg;
		pData++;
		*pData = value;
		pData++;
		ParaListSize += 2;	
		szLine.Empty();
	}
	file.Close();
	return ParaListSize;
}

void MipiRaw10ToP8Raw(BYTE *pIn, USHORT DesW, USHORT DesH)
{
	BYTE *pTemp = pIn;
	BYTE *Pout = pIn;
	USHORT SrcW = DesW*5/4;
	for(USHORT j = 0 ; j < DesH; j++)
	{
		for(USHORT i = 0 ; i <  SrcW; i+=5)
		{
			*Pout++ = pTemp[i];
			*Pout++ = pTemp[i+1];
			*Pout++ = pTemp[i+2];
			*Pout++ = pTemp[i+3];
		}
		pTemp += SrcW;
	}
}

void MipiRaw12ToP8Raw(BYTE *pIn, USHORT DesW, USHORT DesH)
{
	BYTE *Pout = pIn;
	BYTE *pTemp = pIn;
	USHORT SrcW = DesW*3/2;

	for(USHORT j = 0 ; j < DesH; j++)
	{
		for(USHORT i = 0 ; i <  SrcW; i+=3)
		{
			*Pout++ = pTemp[i];
			*Pout++ = pTemp[i+1];
		}
		pTemp += SrcW;
	}
}
void Raw10toRaw8(BYTE *pIn, long number)
{
	BYTE *pTemp = pIn;
	BYTE *pOut = pIn;

	for (long i = 0; i < number; i = i + 5)
	{
		*pOut++ = pTemp[i];
		*pOut++ = pTemp[i + 1];
		*pOut++ = pTemp[i + 2];
		*pOut++ = pTemp[i + 3];
	}
}

void Raw16toRaw8(BYTE *pIn, long number)
{
	BYTE *pTemp = pIn;
	BYTE *pOut = pIn;
	for (long i = 0; i < number; i = i +2)
	{
		*pOut++ = pTemp[i];
	}
}

//20141128 added by leedo....
void MipiRaw10ToWord(BYTE *pIn,WORD *pOut, long number)
{
	int index = 0; 

	//BYTE0 :P1[9:2]
	//BYTE1 :P2[9:2]
	//BYTE2 :P3[9:2]
	//BYTE3 :P4[9:2]
	//BYTE4 :P4[1:0]P3[1:0]P2[1:0]P1[1:0]

	//little endian
	for (long i = 0; i < number; i = i + 5)
	{
		pOut[index++]  = ((WORD)(pIn[i]<< 8)) | (pIn[i+4] & 0x03 );

		pIn[i+4] >>= 2;
		pOut[index++]  = ((WORD)(pIn[i+1]<< 8) ) | (pIn[i+4] & 0x03);

		pIn[i+4] >>= 2;
		pOut[index++]  = ((WORD)(pIn[i+2]<< 8) ) | (pIn[i+4] & 0x03);

		pIn[i+4] >>= 2;
		pOut[index++]  = ((WORD)(pIn[i+3]<< 8) ) | (pIn[i+4] & 0x03);
	} 
}

void MipiRaw10ToP10(BYTE *pIn,BYTE *pOut, long number)
{
	int index = 0; 

	//BYTE0 :P1[9:2]
	//BYTE1 :P2[9:2]
	//BYTE2 :P3[9:2]
	//BYTE3 :P4[9:2]
	//BYTE4 :P4[1:0]P3[1:0]P2[1:0]P1[1:0]

	//little endian
	for (long i = 0; i < number; i = i + 5)
	{
		pOut[index++]  = ((pIn[i  ]<< 2) & 0xfc) | (pIn[i+4] & 0x03 );
		pOut[index++]  = ( pIn[i  ]>> 6) & 0x03;

		pIn[i+4] >>= 2;
		pOut[index++]  = ((pIn[i+1]<< 2) & 0xfc) | (pIn[i+4] & 0x03);
		pOut[index++]  = ( pIn[i+1]>> 6) & 0x03;

		pIn[i+4] >>= 2;
		pOut[index++]  = ((pIn[i+2]<< 2) & 0xfc) | (pIn[i+4] & 0x03);
		pOut[index++]  = ( pIn[i+2]>> 6) & 0x03;

		pIn[i+4] >>= 2;
		pOut[index++]  = ((pIn[i+3]<< 2) & 0xfc) | (pIn[i+4] & 0x03);
		pOut[index++]  = ( pIn[i+3]>> 6) & 0x03;
	} 
}

void Raw12toRaw8(BYTE *pIn, long number)
{

	BYTE *pTemp = pIn;
	BYTE *pOut = pIn;

	for (long i = 0; i < number; i = i +3)
	{
		*pOut++ = pTemp[i];
		*pOut++ = pTemp[i + 1];
	}
}


//���Ϊ4��������
USHORT GetTrueSizeOfPixel(USHORT SizeInPixel, BYTE SensorType)
{
	USHORT SizeInBytes = SensorType == D_MIPI_RAW10 ? (SizeInPixel *5 /4) /20 *20 :
		SensorType == D_RAW10 ? (SizeInPixel *5 /4) /20 *20 :
		SensorType == D_MIPI_RAW12 ? (SizeInPixel *3 /2) /12 *12 : 
		SensorType == D_MIPI_RAW8 ? SizeInPixel/4*4 : SizeInPixel/2*4;	
return SizeInBytes;
}

//���Ϊ2��������
USHORT GetTrueSizeOfPixel2(USHORT SizeInPixel, BYTE SensorType)
{
	USHORT SizeInBytes = SensorType == D_MIPI_RAW10 ? (SizeInPixel *5 /4) /10 *10 :
		SensorType == D_RAW10 ? (SizeInPixel *5 /4) /10 *10 :
		SensorType == D_MIPI_RAW12 ? (SizeInPixel *3 /2) /6 *6 : 
		SensorType == D_MIPI_RAW8 ? SizeInPixel/2*2 : SizeInPixel/2*4;	
return SizeInBytes;
}

USHORT GetPixelSizeOfData(USHORT SizeInBytes, BYTE SensorType)
{
	USHORT SizeInPixels;
	switch(SensorType)
	{
	case D_MIPI_RAW10:
	case D_RAW10:	
		SizeInPixels = SizeInBytes * 4 /5;
		break;
	case D_MIPI_RAW12:
		SizeInPixels = SizeInBytes * 2 /3;
		break;
	case D_YUV:
	case D_YUV_MTK_S:
	case D_YUV_SPI:
	case D_RGB565:
		SizeInPixels = SizeInBytes / 2; //yuv
		break;
	case D_RAW8:
	default:
		SizeInPixels = SizeInBytes;  //8bit
		break;
	}
	return SizeInPixels;
}

void ResetExpGain(pExp_Gain_Tab pTab)
{
	pTab->ExpRegNum = 0;
	pTab->GainRegNum = 0;
	memset(pTab->ExpReg, EXP_GAIN_DATA_EMPTY, sizeof(pTab->ExpReg));
	memset(pTab->GainReg, EXP_GAIN_DATA_EMPTY, sizeof(pTab->GainReg));
	memset(pTab->Exp_Range, EXP_GAIN_DATA_EMPTY, sizeof(pTab->Exp_Range));
	memset(pTab->Gain_Range, EXP_GAIN_DATA_EMPTY, sizeof(pTab->Gain_Range));
	memset(pTab->Func_ExpGain, EXP_GAIN_DATA_EMPTY, sizeof(pTab->Func_ExpGain));
}


UINT WriteSensorCurrentExpGainToIni(CString sSensorName, pExp_Gain_Tab pTab, int State)
{
	SetIniFileNameInExePath("dt_exp_gain.ini");
	State = min(State, FUNC_GROUP_MAX - 1);
	CString sSectKey;
	CString sValue;
	sSectKey.Format("func%d", State);
	sValue.Format("0x%x, 0x%x,  %d, %d, %d", pTab->Func_ExpGain[FUNC_ELEMENT*State],     //exptime
											pTab->Func_ExpGain[FUNC_ELEMENT*State + 1],//analog gain 
											pTab->Func_ExpGain[FUNC_ELEMENT*State + 2],//wb digital Red gain 
											pTab->Func_ExpGain[FUNC_ELEMENT*State + 3],//wb digital Green gain
											pTab->Func_ExpGain[FUNC_ELEMENT*State + 4]);//wb digital Blue Gain
	WriteIniString(sSensorName, sSectKey, sValue);

	ClearIniFileName();
	return 0;
}

UINT LoadSensorCurrentExpGainFromIni(CString sSensorName, pExp_Gain_Tab pTab, int State)
{
	SetIniFileNameInExePath("dt_exp_gain.ini");
	State = min(State, FUNC_GROUP_MAX-1);
	CString sSectKey;
	sSectKey.Format("func%d", State);
	ReadSensorExpGainIniSection(sSensorName, sSectKey, pTab->Func_ExpGain + FUNC_ELEMENT*State, FUNC_ELEMENT);
	ClearIniFileName();
	return 0;
}

UINT LoadSensorExpGainFromIni(CString sSensorName, pExp_Gain_Tab pTab)
{
	SetIniFileNameInExePath("dt_exp_gain.ini");

	int i;
	CString stmp;
	
	pTab->ExpRegNum = ReadSensorExpGainIniSection(sSensorName, "exp_reg", pTab->ExpReg, sizeof(pTab->ExpReg)/sizeof(int));
	pTab->GainRegNum = ReadSensorExpGainIniSection(sSensorName, "gain_reg", pTab->GainReg, sizeof(pTab->GainReg)/sizeof(int));

	ReadSensorExpGainIniSection(sSensorName, "exp_range", pTab->Exp_Range, sizeof(pTab->Exp_Range)/sizeof(int));
	ReadSensorExpGainIniSection(sSensorName, "gain_range", pTab->Gain_Range, sizeof(pTab->Gain_Range)/sizeof(int));

	for(i = 0; i < FUNC_GROUP_MAX; i++)
	{
		stmp.Format("func%d", i);
		ReadSensorExpGainIniSection(sSensorName, stmp, pTab->Func_ExpGain + FUNC_ELEMENT*i, FUNC_ELEMENT);
	}

	ClearIniFileName();

	return 0;
}

UINT ReadSensorExpGainIniSection(CString sSensorName, CString sSection, UINT* pBuffer, int MaxNum)
{
	if(pBuffer == NULL)
	{
		return 0;
	}
	CString stmp,sSect,sRight;
	CString sLine;
	UINT nvalue = 0;

	UINT Count = 0;
	int i;
	sLine = ReadIniString(sSensorName, sSection, "");
	if(!sLine.IsEmpty())
	{
		for(i = 0; i <MaxNum; i++)
		{
			if(AfxExtractSubString(stmp, sLine, i, ','))
			{
				stmp.Trim();
				if(stmp.IsEmpty())
				{
					break;
				}
				stmp.MakeLower();
				if(!sscanf_s(stmp, "0x%x", &nvalue)) //��ȡ��ֵ������	
					sscanf_s(stmp, "%d", &nvalue);
				pBuffer[Count] = nvalue;
				Count++;
			}
			else
			{
				break;
			}
		}
	}
	return Count;
}

void ShowFocusArea(BYTE *pBmp, int width, int height, CPoint AFArea)
{
	int i,j;
	ULONG k;
	//high line
	for(j = AFArea.y - FOCUS_AREA_H-FOCUS_AREA_BORDER; j < AFArea.y - FOCUS_AREA_H+FOCUS_AREA_BORDER; j++)
	{
		i = AFArea.x - FOCUS_AREA_W;
		k = (width* j + i)*3;
		for(; i < AFArea.x+FOCUS_AREA_W; i++)
		{
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
		}
	}
	//low line
	for(j = AFArea.y + FOCUS_AREA_H-FOCUS_AREA_BORDER; j < AFArea.y + FOCUS_AREA_H+FOCUS_AREA_BORDER; j++)
	{
		i = AFArea.x - FOCUS_AREA_W;
		k = (width* j + i)*3;
		for(; i < AFArea.x + FOCUS_AREA_W; i++)
		{
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
		}
	}

	//left line
	for(j = AFArea.y - FOCUS_AREA_H; j < AFArea.y + FOCUS_AREA_H; j++)
	{
		i = AFArea.x - FOCUS_AREA_W-FOCUS_AREA_BORDER;
		k = (width* j + i)*3;
		for(; i < AFArea.x - FOCUS_AREA_W+FOCUS_AREA_BORDER; i++)
		{
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
		}
	}
	//right
	for(j = AFArea.y - FOCUS_AREA_H; j < AFArea.y + FOCUS_AREA_H; j++)
	{
		i = AFArea.x + FOCUS_AREA_W-FOCUS_AREA_BORDER;
		k = (width* j + i)*3;
		for(; i < AFArea.x + FOCUS_AREA_W+FOCUS_AREA_BORDER; i++)
		{
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
			pBmp[k++] = 0xff;
		}
	}
}

//20141127 added...
void CheckDiskInfo()
{
	SetIniFileNameInExePath("enum.ini");

	CString sOldHardDisk = ReadIniString("Serial No", "SN", "");
	sOldHardDisk.Trim();

	CString sCurHardDisk;
	//if(!GetHardIDSerialNo(sCurHardDisk))
	if(!GetMacAddress(sCurHardDisk))
	{
		sCurHardDisk.Empty();
	}
	if(sOldHardDisk != sCurHardDisk)
	{
//		AfxMessageBox(sCurHardDisk);
		CFileFind find;
		if(find.FindFile(sIniFileName())) //���Ҳ�ɾ���ļ�  
		{
			find.Close();
			try
			{
				DeleteFile(sIniFileName());
			}
			catch (CFileException* e)
			{
				e = e;//only for not warings
			}
		}

		WriteIniString("Serial No", "SN", sCurHardDisk);
	}
	ClearIniFileName();
}

void SetIniCurrentDeviceID(int DevID)
{
	m_nIniCurDev = DevID;
	m_sIniFile.Empty();
}
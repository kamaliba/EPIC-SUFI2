
#!/usr/bin/env python
import os
import shutil
import numpy as np
def writeInputData(sInputDir, sSubareaNumber, sCrop, sSpatialDir,sAreaName,rainfedarea_AD,Irrigatearea_AD):
    if os.linesep == "\r\n":
        lineEnd = '\n'
        readCode = "r"
        pathSep = "/"
    elif os.linesep == "\n":
        lineEnd = os.linesep
        readCode = "U"
        pathSep = os.path.sep    
    ### set raster data location
    sDEMPath = sSpatialDir + "dem.asc"
    sSlopePath = sSpatialDir + "slope.asc"
    sSubareaPath = sSpatialDir + "subarea.asc"
    sStudyareaPath = sSpatialDir + "studyarea.asc"
    sSoilPath = sSpatialDir + "soil.asc"
    sClimatePath = sSpatialDir + "climate.asc"
    sRegionalPath = sSpatialDir + "Regional.txt"
        
    ### Get studyarea.asc information
    fStudyAreaText = open(sStudyareaPath, readCode)
    colNum = int(fStudyAreaText.readline().strip(os.linesep).split()[1])
    rowNum = int(fStudyAreaText.readline().strip(os.linesep).split()[1])
    xLeftCor = float(fStudyAreaText.readline().strip(os.linesep).split()[1])
    yBottomCor = float(fStudyAreaText.readline().strip(os.linesep).split()[1])
    resolution = float(fStudyAreaText.readline().strip(os.linesep).split()[1])
    xRightCor = xLeftCor + resolution*colNum
    yUpCor = yBottomCor + resolution*rowNum
    fStudyAreaText.close()
    ### Read the DEM dataset
    demData = readSpatialData(sDEMPath, xLeftCor, yUpCor, colNum, rowNum)    
    ### Read the Slope dataset
    slopeData = readSpatialData(sSlopePath, xLeftCor, yUpCor, colNum, rowNum)
    ### Read the Subarea dataset
    subareaData = readSpatialData(sSubareaPath, xLeftCor, yUpCor, colNum, rowNum)
    ### Read the Studyarea dataset
    studyareaData = readSpatialData(sStudyareaPath, xLeftCor, yUpCor, colNum, rowNum)
    ### Read the Soil dataset
    soilData = readSpatialData(sSoilPath, xLeftCor, yUpCor, colNum, rowNum)
    ### Read the Slope dataset
    climateData = readSpatialData(sClimatePath, xLeftCor, yUpCor, colNum, rowNum)
    rainfedarea=readSpatialData(rainfedarea_AD, xLeftCor, yUpCor, colNum, rowNum)
    Irrigatearea=readSpatialData(Irrigatearea_AD, xLeftCor, yUpCor, colNum, rowNum)
    ### Write data
    sInputDir = "Simulation\\Input" + pathSep + sInputDir + pathSep
    sInputFileName = sSubareaNumber + "_Input.txt"
    fInputFileName = open(sInputDir + sInputFileName, 'wb')
    line = 1

    for i in range(rowNum):
        for j in range(colNum):
            if subareaData[i,j] == int(sSubareaNumber):
                Btemp=0
                if rainfedarea[i,j]==0 and Irrigatearea[i,j]==0:
                    Btemp=1
                if climateData[i,j] > 0 and soilData[i,j] > 0 and studyareaData[i,j] > 0 and Btemp==0:
                    lon = str(xLeftCor+(j+0.5)*resolution)
                    lat = str(yUpCor-(i+0.5)*resolution)
                    temp=[]
                    temp.append(str(line))
                    temp.append(lon)
                    temp.append(lat)
                    temp.append(str(demData[i,j]))
                    temp.append(str(slopeData[i,j]))
                    temp.append(str(soilData[i,j]))
                    temp.append(str(climateData[i,j]))
                    temp.append(str(subareaData[i,j]))
                    temp.append(str(rainfedarea[i,j]))
                    temp.append(str(Irrigatearea[i,j]))
                    Region=calculateVar(yUpCor-(i+0.5)*resolution, xLeftCor+(j+0.5)*resolution,sRegionalPath)
                    temp.append(str(Region))
                    sep=' '
                    temp=sep.join(temp)
                    fInputFileName.write(temp + lineEnd)
                    line += 1
    fInputFileName.close()
    ### Remove the null input.txt file and write the inputList.txt file
    if os.path.getsize(sInputDir + sInputFileName) == 0: 
        os.remove(sInputDir + sInputFileName)
    else:
        sInputList = sInputDir + "inputList.txt"
        fInputList = open(sInputList, 'a')
        fInputList.write(sInputFileName + ',' + str(sAreaName) + ", " + "\n")
        fInputList.close()
    ##############################################

def readSpatialData(filePath, xLeftCor, yUpCor, colNum, rowNum):
    ### filePath: rasterfile path name
    ### Setting for different OS
    if os.linesep == "\r\n":
        lineEnd = '\n'
        readCode = "r"
        pathSep = "/"
    elif os.linesep == "\n":
        lineEnd = os.linesep
        readCode = "U"
        pathSep = os.path.sep
    ### Get header information
    f = open(filePath, readCode)
    nCol = int(f.readline().strip(os.linesep).split()[1])
    nRow = int(f.readline().strip(os.linesep).split()[1])
    xCor = float(f.readline().strip(os.linesep).split()[1])
    yCor = float(f.readline().strip(os.linesep).split()[1])
    cellSize = float(f.readline().strip(os.linesep).split()[1])
    noData = float(f.readline().strip(os.linesep).split()[1])
    f.close()
    ### Generate the value
    value = np.genfromtxt(filePath, skip_header=6)
    rowOri = int((yUpCor-(yCor+nRow*cellSize))/cellSize)
    colOri = int((xCor-xLeftCor)/cellSize)    
    rasterData = np.zeros((nRow, nCol))
    for i in range(nRow):
        for j in range(nCol):
            if value[i,j] >= 0:
                rasterData[rowOri+i,colOri+j] = value[i,j]
    return rasterData
def calculateVar(X, Y, Varfile):
    Var=1
    f = open(Varfile, "U")
    while True:
        data = f.readline()
        if data:
            if data =="\\n":
                continue
            else:
                data = data.strip(os.linesep).split()
                yIn = float(data[0])
                xIn = float(data[1])
                VarIn = float(data[2])
                if yIn == Y and xIn == X:
                    Var=VarIn
                else:
                    continue
        else:
            break
    return Var
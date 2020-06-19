

from pbxproj import XcodeProject
from pbxproj.pbxextensions.ProjectFiles import FileOptions
from pbxproj import PBXList

import sys
import os
import plistlib
import re

class PFiles:
    _FILE_TYPES = {
        '': ('text', 'PBXResourcesBuildPhase'),
        '.a': ('archive.ar', 'PBXFrameworksBuildPhase'),
        '.app': ('wrapper.application', None),
        '.s': ('sourcecode.asm', 'PBXSourcesBuildPhase'),
        '.c': ('sourcecode.c.c', 'PBXSourcesBuildPhase'),
        '.cpp': ('sourcecode.cpp.cpp', 'PBXSourcesBuildPhase'),
        '.framework': ('wrapper.framework', 'PBXFrameworksBuildPhase'),
        '.h': ('sourcecode.c.h', 'PBXHeadersBuildPhase'),
        '.hpp': ('sourcecode.c.h', 'PBXHeadersBuildPhase'),
        '.pch': ('sourcecode.c.h', 'PBXHeadersBuildPhase'),
        '.d': ('sourcecode.dtrace', 'PBXSourcesBuildPhase'),
        '.def': ('text', 'PBXResourcesBuildPhase'),
        '.swift': ('sourcecode.swift', 'PBXSourcesBuildPhase'),
        '.icns': ('image.icns', 'PBXResourcesBuildPhase'),
        '.m': ('sourcecode.c.objc', 'PBXSourcesBuildPhase'),
        '.j': ('sourcecode.c.objc', 'PBXSourcesBuildPhase'),
        '.mm': ('sourcecode.cpp.objcpp', 'PBXSourcesBuildPhase'),
        '.nib': ('wrapper.nib', 'PBXResourcesBuildPhase'),
        '.plist': ('text.plist.xml', 'PBXResourcesBuildPhase'),
        '.json': ('text.json', 'PBXResourcesBuildPhase'),
        '.png': ('image.png', 'PBXResourcesBuildPhase'),
        '.jpg': ('image.jpg', 'PBXResourcesBuildPhase'),
        '.rtf': ('text.rtf', 'PBXResourcesBuildPhase'),
        '.tiff': ('image.tiff', 'PBXResourcesBuildPhase'),
        '.txt': ('text', 'PBXResourcesBuildPhase'),
        '.xcodeproj': ('wrapper.pb-project', None),
        '.xib': ('file.xib', 'PBXResourcesBuildPhase'),
        '.strings': ('text.plist.strings', 'PBXResourcesBuildPhase'),
        '.bundle': ('wrapper.plug-in', 'PBXResourcesBuildPhase'),
        '.dylib': ('compiled.mach-o.dylib', 'PBXFrameworksBuildPhase'),
        '.xcdatamodeld': ('wrapper.xcdatamodel', 'PBXSourcesBuildPhase'),
        '.xcassets': ('folder.assetcatalog', 'PBXResourcesBuildPhase'),
        '.xcconfig': ('sourcecode.xcconfig', 'PBXSourcesBuildPhase'),
        '.tbd': ('sourcecode.text-based-dylib-definition', 'PBXFrameworksBuildPhase'),
        '.bin': ('archive.macbinary', 'PBXResourcesBuildPhase'),
        '.mlmodel':('file.mlmodel', 'PBXSourcesBuildPhase'),
        '.html':('text.html', 'PBXResourcesBuildPhase'),
        '.entitlements': ('text.plist.entitlements', 'PBXResourcesBuildPhase')
    }
    _SPECIAL_FOLDERS = [
        '.bundle',
        '.framework',
        '.xcodeproj',
        '.xcassets',
        '.xcdatamodeld',
        '.storyboardc'
    ]

def set_project(prejectFolderPath,prejectPath,plistInfoDic):
    projectPath = prejectPath + "/project.pbxproj"
    project = XcodeProject.load(projectPath)
    #set_bundle
    set_bundle(project)

    #set_search_paths
    set_search_paths(project)
    #add_folder
    folderPath = prejectFolderPath + "/VigameLibraries/vigame"
    add_folder(project,folderPath)
    # project.add_folder(path = folderPath)

    print("add_folder:",folderPath)

    #add VigameLibrary.plist
    vigameLibraryPlistPath = prejectFolderPath + "/VigameLibraries/VigameLibrary.plist"
    if len(project.get_files_by_name(name = "VigameLibrary.plist")) < 1:
         project.add_file(path = vigameLibraryPlistPath,parent = None)
    print("add_VigameLibrary.plist:",vigameLibraryPlistPath)
     
    #set VigameLibrary.plist 
    set_plist(vigameLibraryPlistPath,plistInfoDic)


    print("Auto Configuration Complete")
    project.save()


def set_search_paths(project):
    #add_header_search_paths
    header_search_paths  =["$(SRCROOT)/VigameLibraries/vigame","$(SRCROOT)/VigameLibraries/deps/boost/include","$(SRCROOT)/VigameLibraries/deps/curl/include/ios","$(SRCROOT)/VigameLibraries/deps/openssl/include/ios","$(SRCROOT)/VigameLibraries/deps/openssl/include/ios","$(SRCROOT)/VigameLibraries/deps/zlib/include/linux"]
    project.add_header_search_paths(paths=header_search_paths,recursive=False)
    print("add_header_search_paths:",header_search_paths)
    #add_library_search_paths
    library_search_paths=["$(PROJECT_DIR)/VigameLibraries/deps/boost/prebuilt/ios","$(PROJECT_DIR)/VigameLibraries/deps/zlib/prebuilt/mac","$(PROJECT_DIR)/VigameLibraries/deps/curl/prebuilt/ios","$(PROJECT_DIR)/VigameLibraries/deps/openssl/prebuilt/ios","$(PROJECT_DIR)/VigameLibraries/deps/curl/prebuilt/mac","$(PROJECT_DIR)/VigameLibraries/deps/openssl/prebuilt/mac","$(PROJECT_DIR)/VigameLibraries/deps/openssl/prebuilt/linux/64-bit"]
    project.add_library_search_paths(paths=library_search_paths,recursive=False)
    print("add_library_search_paths:",library_search_paths)

def get_PBXNativeTarget(project):
    rootObject = project["rootObject"]
    target = project["objects"][rootObject]["targets"][0]
    PBXNativeTarget = project["objects"][target]["buildConfigurationList"]
    return PBXNativeTarget

def set_bundle(project):
    bundleID = "KTM.test4"
    bundleVersion = "1.02"
    displayName = "test1"
    
    PBXNativeTarget = get_PBXNativeTarget(project)
    buildConfigurations = project["objects"][PBXNativeTarget]["buildConfigurations"]
    for buildC in buildConfigurations:
        project["objects"][buildC]["buildSettings"]["PRODUCT_BUNDLE_IDENTIFIER"] = bundleID
        project["objects"][buildC]["buildSettings"]["MARKETING_VERSION"] = bundleVersion
        project["objects"][buildC]["buildSettings"]["PRODUCT_NAME"] = displayName

    print("set_bundleId",bundleID)


def set_plist(plistPath,plistDic):
    print("set_plist",plistDic)
    if os.path.isfile(plistPath):
        print("plist_path:",plistPath)
    with open(plistPath, 'rb') as fp:
        plist = plistlib.load(fp,fmt=None,use_builtin_types=True,dict_type=dict)
        for (k,v) in  plistDic.items():
            plist[k] = v
        # print(plist)
        # print(type(plist))
    with open(plistPath,'wb') as fp:
        #更新plist sort_keys 是否排序
       plistlib.dump(value=plist,fp=fp, fmt=plistlib.FMT_XML, sort_keys=True, skipkeys=False)


def add_folder(project,path, parent=None, excludes=None, recursive=True, create_groups=True, target_name=None,
                   file_options=FileOptions()):
        if not os.path.isdir(path):
            return None

        if not excludes:
            excludes = []

        results = []

        # add the top folder as a group, make it the new parent
        path = os.path.abspath(path)
        if not create_groups and os.path.splitext(path)[1] not in PFiles._SPECIAL_FOLDERS:
            return project.add_file(path, parent, target_name=target_name, force=False, file_options=file_options)

        parent = project.get_or_create_group(os.path.split(path)[1], path, parent)

        # iterate over the objects in the directory
        for child in os.listdir(path):
            # exclude dirs or files matching any of the expressions
            if [pattern for pattern in excludes if re.match(pattern, child)]:
                continue

            full_path = os.path.join(path, child)
            children = []
            if os.path.isfile(full_path) or os.path.splitext(child)[1] in PFiles._SPECIAL_FOLDERS or \
                    not create_groups:
                # check if the file exists already, if not add it
                children = project.add_file(full_path, parent, tree = None,target_name=target_name, force=False,
                                         file_options=file_options)
            else:
                # if recursive is true, go deeper, otherwise create the group here.
                if recursive:
                    children = add_folder(project,full_path, parent, excludes, recursive, target_name=target_name,
                                               file_options=file_options)
                else:
                    project.get_or_create_group(child, child, parent)

            results.extend(children)

        return results

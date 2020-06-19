//
//  ViewController.swift
//  KTMRobot
//
//  Created by liuyaqiang on 2020/6/15.
//  Copyright © 2020 KTM. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }

    @IBAction func press(_ sender: Any) {
        let pro = Process()
        pro.launchPath = "/bin/bash"
        pro.arguments = ["-c", "pwd; which python3; python3 -V; python3 /Users/liuyaqiang/Desktop/GitHub/KTMRobot/test1.py; say over"]
        
//        pro.arguments = ["-c","python3 /Users/liuyaqiang/Desktop/GitHub/iOS_script/python/mysql.py"]
        // 启动
       pro.launch()
       pro.waitUntilExit()

       print("脚本执行完毕")
//        let myAppleScript = "python3 /Users/liuyaqiang/Desktop/GitHub/iOS_script/python/mysql.py"
//        var error: NSDictionary?
//        if let scriptObject = NSAppleScript(source: myAppleScript) {
//            if let output: NSAppleEventDescriptor = scriptObject.executeAndReturnError(&error) {
//                print(output.stringValue)
//            } else if (error != nil) {
//                print("error: \(error)")
//            }
//        }
    }
    
}


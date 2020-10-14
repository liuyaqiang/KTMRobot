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
        CommandRunner.sync(command: "/Users/liuyaqiang/Desktop/GitHub/KTMRobot/auto.sh")
    }
}


//
//  ContentView.swift
//  SumsMLApp
//
//  Created by Ayush Deolasee on 04/03/23.
//

import SwiftUI
import CoreML

struct ContentView: View {
    @State private var number1: String = "";
    @State private var number2: String = "";
    @State private var sum: String = "";
    
    func calculateSum(num1: Double, num2: Double) {
        do {
            let config = MLModelConfiguration()
            let model = try SumClassification(configuration: config)
            
            let prediction = try model.prediction(Number_1: num1, Number_2: num2)
            sum = String(prediction.Sum)
            
        } catch {
            print("Some error")
        }
    }
    var body: some View {
        VStack {
            Form {
                TextField("Number 1", text:$number1)
                TextField("Number 2", text: $number2)
            }
            .frame(height: 150)
            Button("Compute") {
                let modelNumber1: Double = Double(number1) ?? 0;
                let modelNumber2: Double = Double(number2) ?? 0;
                calculateSum(num1: modelNumber1, num2: modelNumber2)
                
            }
        
            Text(sum)
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

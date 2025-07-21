"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function Component() {
  const [display, setDisplay] = useState("0")

  const handleButtonClick = () => {
    setDisplay((prev) => (prev === "0" ? "חוח" : prev + " חוח"))
  }

  const handleClear = () => {
    setDisplay("0")
  }

  const calculatorButtons = [
    ["C", "±", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="],
  ]

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <Card className="w-full max-w-sm shadow-2xl">
        <CardHeader className="text-center pb-4">
          <CardTitle className="text-2xl font-bold text-gray-800">מחשבון חוח</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          {/* Display */}
          <div className="bg-black text-white p-4 rounded-lg text-right text-2xl font-mono min-h-[60px] flex items-center justify-end overflow-hidden">
            {display}
          </div>

          {/* Calculator Buttons */}
          <div className="grid gap-2">
            {calculatorButtons.map((row, rowIndex) => (
              <div key={rowIndex} className="grid grid-cols-4 gap-2">
                {row.map((button, buttonIndex) => {
                  const isZero = button === "0"
                  const isClear = button === "C"
                  const isOperator = ["÷", "×", "-", "+", "="].includes(button)
                  const isSpecial = ["±", "%"].includes(button)

                  return (
                    <Button
                      key={buttonIndex}
                      onClick={isClear ? handleClear : handleButtonClick}
                      className={`
                        h-14 text-lg font-semibold transition-all duration-200 hover:scale-105 active:scale-95
                        ${isZero ? "col-span-2" : ""}
                        ${isClear ? "bg-gray-500 hover:bg-gray-600 text-white" : ""}
                        ${isOperator ? "bg-orange-500 hover:bg-orange-600 text-white" : ""}
                        ${isSpecial ? "bg-gray-400 hover:bg-gray-500 text-white" : ""}
                        ${!isClear && !isOperator && !isSpecial ? "bg-gray-200 hover:bg-gray-300 text-black" : ""}
                      `}
                    >
                      {button}
                    </Button>
                  )
                })}
              </div>
            ))}
          </div>

          <div className="text-center text-sm text-gray-600 mt-4">לחץ על כל כפתור לקבלת הפתעה! 😄</div>
        </CardContent>
      </Card>
    </div>
  )
}

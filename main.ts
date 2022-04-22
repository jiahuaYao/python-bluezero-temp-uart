bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    uartData = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
    basic.showString(uartData)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
})
let uartData = ""
bluetooth.startTemperatureService()
bluetooth.startUartService()
basic.showLeds(`
    # . . . .
    # . . . .
    # . . . .
    # . . . .
    # # # # #
    `)

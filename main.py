def on_bluetooth_connected():
    global uartData
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    basic.show_string(uartData)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

uartData = ""
bluetooth.start_temperature_service()
bluetooth.start_uart_service()
basic.show_leds("""
    # . . . .
        # . . . .
        # . . . .
        # . . . .
        # # # # #
""")
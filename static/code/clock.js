function __python__UpdateClockData() {
    const clock_node = document.querySelector('.__python__clock-node')
    if (!clock_node) return

    const [date, time] = (new Date()).toLocaleString().split(' ')
    
    clock_node.querySelector('.__python__clock-date').textContent = date
    clock_node.querySelector('.__python__clock-time').textContent = time
}

setInterval(__python__UpdateClockData, 1);
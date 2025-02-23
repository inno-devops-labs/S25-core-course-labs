import { useState, useEffect } from 'react'
import './SummerCountdown.css'

const SummerCountdown = () => {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0
  })

  useEffect(() => {
    const calculateTime = () => {
      const now = new Date()
      const summer = new Date(now.getFullYear(), 5, 1) // 1st july
      
      if (now > summer) {
        summer.setFullYear(summer.getFullYear() + 1)
      }

      const diff = summer.getTime() - now.getTime()

      setTimeLeft({
        days: Math.floor(diff / (1000 * 60 * 60 * 24)),
        hours: Math.floor((diff / (1000 * 60 * 60)) % 24),
        minutes: Math.floor((diff / 1000 / 60) % 60),
        seconds: Math.floor((diff / 1000) % 60)
      })
    }

    calculateTime()
    const timer = setInterval(calculateTime, 1000)
    return () => clearInterval(timer)
  }, [])

  return (
    <div className="countdown-container">
      <h1 className="countdown-title">Summer countdown!</h1>
      <div className="countdown-timer">
        <div className="countdown-block">
          <div className="countdown-number">{timeLeft.days}</div>
          <div className="countdown-label">days</div>
        </div>
        <div className="countdown-block">
          <div className="countdown-number">{timeLeft.hours}</div>
          <div className="countdown-label">hours</div>
        </div>
        <div className="countdown-block">
          <div className="countdown-number">{timeLeft.minutes}</div>
          <div className="countdown-label">minutes</div>
        </div>
        <div className="countdown-block">
          <div className="countdown-number">{timeLeft.seconds}</div>
          <div className="countdown-label">seconds</div>
        </div>
      </div>
    </div>
  )
}

export default SummerCountdown
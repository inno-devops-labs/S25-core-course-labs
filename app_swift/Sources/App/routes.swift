import Vapor
import SwiftDate

func routes(_ app: Application) throws {
    // Define the route to show current Moscow time
    app.get { req -> EventLoopFuture<View> in
        // Initialize the Moscow region with TimeZone, Calendar, and Locale
        let moscowRegion = Region(
            calendar: Calendar(identifier: .gregorian),  // Use the correct Calendar identifier
            zone: TimeZone(identifier: "Europe/Moscow")!,  // Correct way to set Moscow time zone
            locale: Locale(identifier: "en_US")  // Correct locale identifier
        )
        
        // Get the current date and time in the Moscow region
        let moscowTime = DateInRegion()  // Current date and time
        let moscowTimeInRegion = moscowTime.convertTo(region: moscowRegion)  // Convert it to Moscow region
        
        // Format the time to the desired format
        let formattedTime = moscowTimeInRegion.toFormat("yyyy-MM-dd HH:mm:ss")
        
        // Render the view with the formatted time
        return req.view.render("index", ["time": formattedTime])
    }
}

import java.io.File

fun transformFileContent(fileContent: String): List<Pair<Int, Int>> {
    val lines = fileContent.split("\n")
    val time = lines[0].split(":")[1].trim().split("\\s+".toRegex()).map { it.toInt() }
    val distance = lines[1].split(":")[1].trim().split("\\s+".toRegex()).map { it.toInt() }
    return time.zip(distance)
}

fun main(args: Array<String>) {
    val filePath = "src/main/kotlin/input.txt"
    val fileContent = File(filePath).readText()

    val raceDetails = transformFileContent(fileContent)
    println(raceDetails)


    var totalWays = 1
    for ((time, distanceToBeat) in raceDetails) {
        var waysToBeat = 0
        //println("Time: $time, Distance: $distance")
        //This loop marks how much time (speed) the button is pressed
        for (speed in 1..<time) {
            val distance = speed * (time - speed)
            if(distance > distanceToBeat) {
                waysToBeat++
            }
        }
        totalWays *= waysToBeat
    }

    println(totalWays)
}
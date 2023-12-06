import java.io.File

fun transformFileContent(fileContent: String): Pair<Long, Long> {
    val lines = fileContent.split("\n")
    val time = lines[0].split(":")[1].trim().replace(" ", "").toLong()
    val distance = lines[1].split(":")[1].trim().replace(" ", "").toLong()
    return Pair(time, distance)
}

fun main(args: Array<String>) {
    val filePath = "src/main/kotlin/input.txt"
    val fileContent = File(filePath).readText()

    val raceDetails = transformFileContent(fileContent)
    println(raceDetails)
    val time = raceDetails.first
    val distanceToBeat = raceDetails.second

    var waysToBeat = 0

    //This loop marks how much time (speed) the button is pressed
    for (speed in 1..<time) {
        val distance = speed * (time - speed)
        if(distance > distanceToBeat) {
            waysToBeat++
        }
    }


    println(waysToBeat)
}
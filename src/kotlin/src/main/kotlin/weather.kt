package me.silent

import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.jsonObject

private const val key = "7be1f4f13ae9483c08b4762c1f473765"
private const val url = "https://api.openweathermap.org/data/2.5/weather?lat=60&lon=10&appid=$key&units=metric"

suspend fun getWeatherInfo(): String {
    val data = (getAndCheck(url) as JsonObject)["main"]!!.jsonObject
    val temp = data["temp"].toString().toDouble()
    return "The temperature is $temp degrees celsius"
}
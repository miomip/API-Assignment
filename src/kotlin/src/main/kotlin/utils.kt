package me.silent

import io.ktor.client.request.get
import io.ktor.client.statement.bodyAsText
import io.ktor.http.HttpStatusCode
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.jsonObject

suspend fun getAndCheck(url: String, ind: String = "json"): Any {
    val request = client.get(url)

    if (request.status != HttpStatusCode.OK) {
        throw RuntimeException("Request failed with status code: ${request.status}")
    }
    if (ind.lowercase() == "string")
        return request.bodyAsText()
    return Json.parseToJsonElement(request.bodyAsText()).jsonObject
}
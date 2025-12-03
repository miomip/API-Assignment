package me.silent

import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.coroutines.runBlocking
import kotlin.properties.Delegates

val client = HttpClient(CIO) {
    install(ContentNegotiation) {
        json()
    }
}

val operations = mapOf<String, suspend ()-> String>(
    "pokemon" to ::getPokemon,
    "weather" to ::getWeatherInfo,
    "catfact" to ::getCatFact
)

fun main(args: Array<String>): Unit = runBlocking {
    var input by Delegates.notNull<String>()
    while (true) {
        print("What do you want to do? ")
        input = readln().lowercase()
        if (input !in operations) continue
        break
    }
    println(operations[input]!!())
}



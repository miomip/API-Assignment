package me.silent

import kotlinx.serialization.json.JsonObject

suspend fun getPokemon(): String {
    print("Pokemon name: ")
    val pokemon = readln()
    val url = "https://pokeapi.co/api/v2/pokemon/$pokemon"

    val data = getAndCheck(url) as JsonObject

    val height = data["height"].toString().toDouble() / 10
    val weight = data["weight"].toString().toDouble() / 10

    return "Height is $height meters\nand it weighs $weight kg"
}
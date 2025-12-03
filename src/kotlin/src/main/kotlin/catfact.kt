package me.silent

private const val url = "https://catfat.ninja/fact"

suspend fun getCatFact(): String {
    return getAndCheck(url, "string") as String
}
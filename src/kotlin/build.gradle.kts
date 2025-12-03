plugins {
    kotlin("jvm") version "2.2.21"
    kotlin("plugin.serialization") version "2.2.21"
}
kotlin {
    jvmToolchain(21)
}
dependencies {
    implementation("io.ktor:ktor-serialization-kotlinx-json:3.3.2")
    implementation("io.ktor:ktor-client-core:3.3.2")
    implementation("io.ktor:ktor-client-cio:3.3.2")
    implementation("io.ktor:ktor-client-content-negotiation:3.3.2")
    implementation("org.slf4j:slf4j-nop:2.0.9")
}
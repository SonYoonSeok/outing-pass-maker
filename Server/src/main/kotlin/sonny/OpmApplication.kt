package sonny

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class OpmApplication

fun main(args: Array<String>) {
	runApplication<OpmApplication>(*args)
}

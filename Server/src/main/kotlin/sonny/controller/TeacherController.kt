package sonny.controller

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController
import sonny.entity.Teacher
import sonny.response.TeacherListResponse
import sonny.service.TeacherService

@RestController
@RequestMapping("/api")
class TeacherController(
    val teacherService: TeacherService
) {
    @GetMapping("/teachers")
    fun findTeacherListByYear(@RequestParam(value = "year", required = true) year: String): TeacherListResponse {
        return teacherService.findAllTeacherByYear(year)
    }
}
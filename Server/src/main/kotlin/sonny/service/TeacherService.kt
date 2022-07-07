package sonny.service

import org.springframework.stereotype.Service
import sonny.entity.Teacher
import sonny.entity.TeacherRepository
import sonny.response.TeacherListResponse

@Service
class TeacherService(
    val teacherRepository: TeacherRepository
) {
    fun findAllTeacherByYear(year: String): TeacherListResponse {
        val teachers = teacherRepository.findAllByYear(year)?.let {
            return TeacherListResponse(year, getTeacherList(it))
        } ?: throw Exception("Teacher is not Exist")
    }

    private fun getTeacherList(teachers: List<Teacher>): List<String> {
        var teacherList = arrayListOf<String>()
        for (i in teachers.indices) {
            val teacher = teachers[i]
            teacherList.add(teacher.name)
        }

        return teacherList
    }
}
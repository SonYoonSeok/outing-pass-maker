package sonny.entity

import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface TeacherRepository : CrudRepository<Teacher, Long> {
    fun findAllByYear(year: String): List<Teacher>?
}
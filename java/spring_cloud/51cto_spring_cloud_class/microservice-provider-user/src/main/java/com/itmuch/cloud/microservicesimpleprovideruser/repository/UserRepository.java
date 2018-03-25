package com.itmuch.cloud.microservicesimpleprovideruser.repository;

import com.itmuch.cloud.microservicesimpleprovideruser.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by bwhite on 18-3-4.
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}

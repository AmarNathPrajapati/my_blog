-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2023 at 05:56 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(3) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `phone`, `email`, `message`, `date`) VALUES
(1, 'amar', 912456789, 'amarnath@gmail.com', 'Hi', '2023-04-21'),
(2, 'Chandan', 9786424234, 'chandan@gmail.com', 'this is the message', '2023-04-22'),
(3, 'Chandan', 9786424234, 'chandan@gmail.com', 'this is the message', '2023-04-22'),
(4, 'Chandan', 9786424234, 'amarnathjnp2002@gmail.com', 'this is message from chandan ', '2023-04-22'),
(5, 'Chandan', 9786424234, 'amarnathjnp2002@gmail.com', 'this is message from chandan ', '2023-04-22'),
(6, 'Chandan', 9786424234, 'amarnathjnp2002@gmail.com', 'this is message from chandan ', '2023-04-22'),
(7, 'Chandan', 9786424234, 'amarnathjnp2002@gmail.com', 'this is message from chandan ', '2023-04-22');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(3) NOT NULL,
  `title` text NOT NULL,
  `taglline` text NOT NULL,
  `sub_title` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `taglline`, `sub_title`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'updated title', '', 'this is the subtitle of the updated title', 'updated slug', 'updated content', 'home-bg.jpg', '2023-04-21 19:39:03'),
(2, 'update second ', '', 'this is the subtitle of the new title', 'updated slug', 'this  is the content', 'home-bg.jpg', '2023-04-21 19:41:18'),
(5, 'blog 3', '', 'this is the subtitle of the new title', 'updated slug', 'this is the content', 'home-bg.jpg', '2023-04-22 01:36:58'),
(6, 'blog 4 ', '', 'this is the subtitle of the new title', 'new-slug', 'this is the content for blog 4', 'home-bg.jpg', '2023-04-22 01:37:29'),
(7, 'blog 5', '', 'this is the subtitle of the updated title', 'updated slug', 'this is the content for the blog 5', 'home-bg.jpg', '2023-04-22 01:38:09'),
(8, 'blog 6', '', 'this is the subtitle of the updated title', 'updated slug', 'this is the content for blog 6', 'home-bg.jpg', '2023-04-22 01:38:36');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

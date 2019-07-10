-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2019 a las 21:50:10
-- Versión del servidor: 10.3.16-MariaDB
-- Versión de PHP: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `aver`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `RecomendacionPerfil` (IN `sesion` INT)  NO SQL
SELECT idpeliculas,valor from peliculas
LEFT JOIN
(select sum(val) valor,idpeli from 
(SELECT IdPeli,tabla2.val,idusuario,calificacion from relacionusuariopelis
INNER JOIN
        (SELECT count(*) val,relacionusuariopelis.IdUsuario us from relacionusuariopelis
        INNER JOIN
                (SELECT * from relacionusuariopelis
                WHERE IdUsuario=sesion
                and Calificacion <> 0)objetivo
        on objetivo.idPeli=relacionusuariopelis.IdPeli
        AND objetivo.calificacion=relacionusuariopelis.Calificacion
        WHERE relacionusuariopelis.IdUsuario<>sesion
        GROUP by relacionusuariopelis.IdUsuario) tabla2
on tabla2.us=relacionusuariopelis.IdUsuario) xd
WHERE xd.calificacion=1
group by idpeli , calificacion) tablafinal
ON tablafinal.idpeli=peliculas.idpeliculas
where idpeliculas not in 
	(SELECT idpeli from relacionusuariopelis
    where idusuario=sesion
    and calificacion<>0)
order by tablafinal.valor DESC ,idpeliculas ASC
limit 10$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `RecomendacionQuiz` (IN `sesion` INT)  SELECT idpeliculas,valor from peliculas
LEFT JOIN
(select sum(val) valor,idpeli from 
(SELECT IdPeli,tabla2.val,idusuario,calificacion from relacionusuariopelis
INNER JOIN
        (SELECT count(*) val,relacionusuariopelis.IdUsuario us from relacionusuariopelis
        INNER JOIN
                (SELECT * from relacionusuariopelis
                WHERE IdUsuario=sesion
                and Calificacion <> 0)objetivo
        on objetivo.idPeli=relacionusuariopelis.IdPeli
        AND objetivo.calificacion=relacionusuariopelis.Calificacion
        WHERE relacionusuariopelis.IdUsuario<>sesion
        GROUP by relacionusuariopelis.IdUsuario) tabla2
on tabla2.us=relacionusuariopelis.IdUsuario) xd
WHERE xd.calificacion=1
group by idpeli , calificacion) tablafinal
ON tablafinal.idpeli=peliculas.idpeliculas
where idpeliculas not in 
	(SELECT idpeli from relacionusuariopelis
    where idusuario=sesion)
order by tablafinal.valor DESC ,idpeliculas ASC
limit 10$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `relacionusuariopelis`
--

CREATE TABLE `relacionusuariopelis` (
  `IdRelacion` int(11) NOT NULL,
  `IdUsuario` int(11) NOT NULL,
  `IdPeli` int(11) NOT NULL,
  `Calificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `relacionusuariopelis`
--

INSERT INTO `relacionusuariopelis` (`IdRelacion`, `IdUsuario`, `IdPeli`, `Calificacion`) VALUES
(3, 2, 23, 1),
(4, 2, 41, -1),
(5, 2, 22, 1),
(6, 2, 16, 1),
(7, 2, 2, 1),
(8, 2, 68, -1),
(9, 2, 66, -1),
(10, 2, 54, -1),
(11, 2, 26, -1),
(12, 2, 6, -1),
(13, 1, 62, 1),
(14, 1, 25, 1),
(16, 1, 41, -1),
(17, 1, 22, 1),
(19, 1, 2, -1),
(20, 1, 68, 1),
(21, 1, 66, -1),
(22, 1, 54, 1),
(23, 1, 26, 1),
(24, 1, 6, -1),
(25, 3, 62, 1),
(26, 3, 25, -1),
(27, 3, 23, 1),
(28, 3, 41, 1),
(29, 3, 22, 1),
(30, 3, 16, -1),
(31, 3, 2, 1),
(32, 3, 68, -1),
(33, 3, 66, 1),
(34, 3, 54, 1),
(35, 3, 26, 1),
(36, 3, 6, 1),
(37, 4, 62, 1),
(38, 4, 23, 1),
(39, 4, 41, 1),
(40, 4, 22, 1),
(41, 4, 16, 1),
(42, 4, 2, 1),
(43, 4, 68, 1),
(44, 4, 66, 1),
(45, 4, 54, 1),
(46, 4, 26, 1),
(47, 4, 6, 1),
(91, 1, 9, 1),
(248, 5, 1, 1),
(249, 5, 2, 1),
(250, 5, 3, -1),
(251, 5, 4, -1),
(252, 5, 8, -1),
(253, 5, 7, 1),
(254, 5, 6, -1),
(255, 5, 9, -1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `contraseña` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `respustas` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idusuario`, `nombre`, `contraseña`, `correo`, `respustas`) VALUES
(1, 'Braiunito', 'mypass123', 'braiantablet@gmail.com', NULL),
(2, 'Agustin', '12345678', NULL, NULL),
(3, 'Marcos', '12345678', NULL, NULL),
(4, 'Mateo', '12345678', NULL, NULL),
(5, 'aber', '12345678', NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `relacionusuariopelis`
--
ALTER TABLE `relacionusuariopelis`
  ADD PRIMARY KEY (`IdRelacion`),
  ADD KEY `relacionusuariopelis_ibfk_1` (`IdPeli`),
  ADD KEY `relacionusuariopelis_ibfk_2` (`IdUsuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `relacionusuariopelis`
--
ALTER TABLE `relacionusuariopelis`
  MODIFY `IdRelacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=256;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `relacionusuariopelis`
--
ALTER TABLE `relacionusuariopelis`
  ADD CONSTRAINT `relacionusuariopelis_ibfk_1` FOREIGN KEY (`IdPeli`) REFERENCES `qver`.`peliculas` (`idpeliculas`),
  ADD CONSTRAINT `relacionusuariopelis_ibfk_2` FOREIGN KEY (`IdUsuario`) REFERENCES `usuario` (`idusuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
<<<<<<< HEAD
-- Tiempo de generación: 04-07-2019 a las 21:38:36
-- Versión del servidor: 10.3.15-MariaDB
-- Versión de PHP: 7.1.30
=======
-- Tiempo de generación: 07-07-2019 a las 23:46:14
-- Versión del servidor: 10.3.16-MariaDB
-- Versión de PHP: 7.3.6
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `qver`
--

<<<<<<< HEAD
=======
DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `xd` (IN `sesion` INT)  SELECT idpeliculas,valor from peliculas
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

DELIMITER ;

>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

CREATE TABLE `peliculas` (
  `idpeliculas` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `año` varchar(45) DEFAULT NULL,
  `tags` varchar(45) DEFAULT NULL,
  `descripcion` varchar(1000) DEFAULT NULL,
  `img` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `peliculas`
--

INSERT INTO `peliculas` (`idpeliculas`, `nombre`, `genero`, `año`, `tags`, `descripcion`, `img`) VALUES
(1, 'John Wick 3: Parabellum', 'Accion', '2019', '#thriller#crimen', 'John Wick regresa de nuevo pero con una recompensa sobre su cabeza que persigue unos mercenarios. Tras asesinar a uno de los miembros de su gremio, Wick es expulsado y se convierte en el foco de atención de todos los sicarios de la organización', 'https://m.media-amazon.com/images/M/MV5BMDg2YzI0ODctYjliMy00NTU0LTkxODYtYTNkNjQwMzVmOTcxXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SY1000_CR0,0,648,1000_AL_.jpg'),
(2, 'Avengers:Endgame', 'Accion', '2019', '#aventura#cienciaficcion', 'Los Vengadores restantes deben encontrar una manera de recuperar a sus aliados para un enfrentamiento épico con Thanos, el malvado que diezmó el planeta y el universo.', 'https://pbs.twimg.com/media/D1nmVNuU4AAO2yD.jpg'),
(3, 'X-Men: Fenix Oscura', 'Accion', '2019', '#aventura#cienciaficcion', 'Los X-Men se enfrentan a su enemigo más poderoso: uno de sus miembros, Jean Grey. Durante una misión de rescate en el espacio, Jean casi muere al ser alcanzada por una misteriosa fuerza cósmica. Cuando regresa a casa, esa radiación la ha hecho más poderosa, pero mucho más inestable. Jean cae en una espiral fuera de control haciendo daño a aquellos que más quiere.', 'http://es.web.img3.acsta.net/r_1280_720/pictures/19/05/10/12/27/4446380.jpg'),
(4, 'Godzilla: Rey de los monstruos', 'Accion', '2019', '#aventura#fantasia', 'Godzilla, Rey de los Monstruos, surge para combatir a enemigos enormes y malos que se han estado alimentando con los reactores de una planta nuclear y ahora amenazan a la humanidad con aniquilarla.', 'http://www.mubis.es/media/users/12828/229939/poster-godzilla-ii-rey-de-los-monstruos-original.jpg'),
(5, 'Rocketman', 'Biografia', '2019', '#drama#musica', '\"Rocketman\" cuenta la trayectoria del artista Elton John, desde sus años como niño prodigio del piano en la Royal Academy of Music hasta llegar a ser una superestrella de fama mundial gracias a su talento y a la duradera asociación con su letrista Bernie Taupin.', 'http://es.web.img3.acsta.net/c_215_290/pictures/19/02/19/16/26/1562265.jpg'),
(6, 'Cadena perpetua', 'Drama', '1994', '#encarcelamiento ilícito#escapar de la prisió', 'Dos hombres encarcelados se unen durante varios años, encontrando consuelo y una eventual redención a través de actos de decencia común.', 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(7, 'El padrino', 'Drama', '1972', '#drama#suspenso', 'El anciano patriarca de una dinastía del crimen organizado transfiere el control de su imperio clandestino a su renuente hijo.', 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg'),
(8, 'El padrino: Parte II', 'Drama', '1974', '#drama#suspenso', 'La vida temprana y la carrera de Vito Corleone en la ciudad de Nueva York en 1920 se retrata, mientras que su hijo, Michael, se expande y refuerza su control sobre el sindicato de delitos familiares.', 'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg'),
(9, 'El caballero oscuro', 'Accion', '2008', '#accion#suspenso', 'Cuando la amenaza conocida como The Joker emerge de su pasado misterioso, causa estragos y caos en la gente de Gotham. El Caballero Oscuro debe aceptar una de las mejores pruebas psicológicas y físicas de su capacidad para combatir la injusticia.', 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(10, 'Toy Story 4', 'Animacion', '2019', '#aventura#animacion#comedia', 'Cuando un nuevo juguete llamado \"Forky\" se une a Woody y la pandilla, un viaje por carretera junto a viejos y nuevos amigos revela qué tan grande puede ser el mundo para un juguete.', 'https://m.media-amazon.com/images/M/MV5BMTYzMDM4NzkxOV5BMl5BanBnXkFtZTgwNzM1Mzg2NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(11, 'Spider-Man: Lejos de casa', 'Accion', '2019', '#aventura#cienciaficcion#accion', 'Siguiendo los eventos de Vengadores: Endgame (2019), Spider-Man debe actuar para enfrentar nuevas amenazas en un mundo que ha cambiado para siempre.', 'https://m.media-amazon.com/images/M/MV5BMGZlNTY1ZWUtYTMzNC00ZjUyLWE0MjQtMTMxN2E3ODYxMWVmXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(12, 'Los ángeles de Charlie', 'Accion', '2019', '#aventura#comedia', 'Reinicio de la comedia de acción del 2000 basada en la serie de televisión de los setenta. Una nueva generación de detectives privados trabajando para el misterioso Charlie.', 'https://m.media-amazon.com/images/M/MV5BMDFkNzA3MmMtYTc1Mi00ZWNjLWJjMjctODQ2ZGI2OWY0YmExXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(13, 'Criminales en el mar', 'Accion', '2019', '#comedia#crimen', 'Un policía de Nueva York y su esposa se van de vacaciones en Europa para revitalizar la chispa de su matrimonio, pero terminan enmascarados y huyen por la muerte de un multimillonario anciano.', 'https://m.media-amazon.com/images/M/MV5BNTA2YTI5YjUtZWI4Zi00NWQ5LWFiYmEtOTBmNTUyNDAwNjllXkEyXkFqcGdeQXVyNjIzNzM4NzA@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(14, 'Chucky: El muñeco diabólico', 'Terror', '2019', '#terror#thriller#suspenso', 'Una madre le da a su hijo de 13 años un muñeco de juguete para su cumpleaños, sin darse cuenta de su naturaleza más siniestra.', 'https://m.media-amazon.com/images/M/MV5BNTNlNjIxNjktOWUyMS00YWY5LWEwZGItMjZmODJlZWNiZGM2XkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(15, 'Kabir Singh', 'Romance', '2019', '#romance#drama#amor', 'Kabir Singh es un remake de una película de Telugu Arjun Reddy (2017), donde un cirujano de la casa de mal genio se acostumbra a las drogas y las bebidas cuando su novia se ve obligada a casarse con otra persona.', 'https://m.media-amazon.com/images/M/MV5BOTIyMTNkMWQtZDJlYi00OGJmLTliN2MtOGE0YjY4NzFiYTNmXkEyXkFqcGdeQXVyOTAzMTc2MjA@._V1_UY268_CR6,0,182,268_AL_.jpg'),
(16, 'Annabelle 3: Viene a casa', 'Terror', '2019', '#terror#misterio#thriller', 'Mientras cuidaba a la hija de Ed y Lorraine Warren, una adolescente y su amiga, sin saberlo, despiertan a un espíritu maligno atrapado en una muñeca.', 'https://m.media-amazon.com/images/M/MV5BYmI4NDNiMmQtZTFkYi00ZDVmLThlYTAtMWJlMjU1M2I2ZmViXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(17, 'Yesterday', 'Comedia', '2019', '#comedia#fanasia#musica', 'Un músico que lucha se da cuenta de que es la única persona en la Tierra que puede recordar a los Beatles después de despertarse en una línea de tiempo alternativa donde nunca existieron.', 'https://m.media-amazon.com/images/M/MV5BMjQ0NTI0NjkyN15BMl5BanBnXkFtZTgwNzY0MTE0NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(18, 'Midsommar', 'Drama', '2019', '#horror#misterio', 'Una pareja viaja a Suecia para visitar el fabuloso festival de mediados de verano de una ciudad natal rural. Lo que comienza como un retiro idílico se convierte rápidamente en una competencia cada vez más violenta y extraña a manos de un culto pagano.', 'https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwODM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(19, 'Hombres de Negro: Internacional', 'Accion', '2019', '#aventura#comedia#accion', 'Los Hombres de Negro siempre han protegido a la Tierra de la escoria del universo. En esta nueva aventura, abordan su mayor amenaza hasta la fecha: un lunar en la organización Hombres de Negro.', 'https://m.media-amazon.com/images/M/MV5BMDZkODI2ZGItYTY5Yi00MTA4LWExY2ItM2ZmNjczYjM0NDg1XkEyXkFqcGdeQXVyMzY0MTE3NzU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(20, 'El rey león', 'Animacion', '2019', '#aventura#drama#animacion', 'Después del asesinato de su padre, un joven príncipe león huye de su reino solo para aprender el verdadero significado de la responsabilidad y la valentía.', 'https://m.media-amazon.com/images/M/MV5BMjIwMjE1Nzc4NV5BMl5BanBnXkFtZTgwNDg4OTA1NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(21, 'Érase una vez en... Hollywood', 'Comedia', '2019', '#drama#comedia', 'Un actor de televisión descolorido y su doble se esforzaron por alcanzar la fama y el éxito en la industria del cine durante los últimos años de la Edad de Oro de Hollywood en 1969 en Los Ángeles.', 'https://m.media-amazon.com/images/M/MV5BOTg4ZTNkZmUtMzNlZi00YmFjLTk1MmUtNWQwNTM0YjcyNTNkXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(22, 'Anna', 'Accion', '2019', '#accion#thriller', 'Bajo la sorprendente belleza de Anna Poliatova se encuentra un secreto que desatará su fuerza y ??habilidad indelebles para convertirse en uno de los asesinos gubernamentales más temidos del mundo.', 'https://m.media-amazon.com/images/M/MV5BZjE4M2FjMDQtZGQ5Mi00YTliLWIwZmMtZGJkMjgxYTY5ZTlmXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(23, 'Aladdín', 'Aventura', '2019', '#aventura#comedia#fantasia', 'Un erizo de la calle de buen corazón y un Gran Visir hambriento de poder compiten por una lámpara mágica que tiene el poder de hacer realidad sus deseos más profundos.', 'https://m.media-amazon.com/images/M/MV5BMjQ2ODIyMjY4MF5BMl5BanBnXkFtZTgwNzY4ODI2NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(24, 'Spider-Man: Un nuevo universo', 'Animacion', '2018', '#animacion#accion#aventura', 'El adolescente Miles Morales se convierte en el Hombre Araña de su realidad, cruzando su camino con cinco contrapartes de otras dimensiones para detener una amenaza para todas las realidades.', 'https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(25, 'After: Aquí empieza todo', 'Drama', '2019', '#drama#romance', 'Una mujer joven se enamora de un chico con un secreto oscuro y los dos se embarcan en una relación difícil. Basada en la novela de Anna Todd.', 'https://m.media-amazon.com/images/M/MV5BOGUwMjk3YzktNDI0Yy00MzFiLWFjNmEtYTA2ODVjMzNhODhjXkEyXkFqcGdeQXVyOTQ1MDI4MzY@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(26, 'Brightburn (El hijo)', 'Terror', '2019', '#cienciaficcion#terror', '¿Qué pasaría si un niño de otro mundo aterrizara en la Tierra, pero en lugar de convertirse en un héroe para la humanidad, demostró ser algo mucho más siniestro?', 'https://m.media-amazon.com/images/M/MV5BMjc0YzM2ZjItNzE3OS00NTRhLTkyNTUtMjY5Y2Y5NTU3OWI0XkEyXkFqcGdeQXVyNjU2NTI4MjE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(27, '¡Shazam!', 'Accion', '2019', '#aventura#comedia#accion', 'Todos tenemos un superhéroe dentro de nosotros, solo se necesita un poco de magia para llevarlo a cabo. En el caso de Billy Batson, al gritar una palabra, SHAZAM, este niño adoptivo de catorce años de edad puede convertirse en el superhéroe adulto Shazam.', 'https://m.media-amazon.com/images/M/MV5BYTE0Yjc1NzUtMjFjMC00Y2I3LTg3NGYtNGRlMGJhYThjMTJmXkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(28, 'Yo soy madre', 'Drama', '2019', '#terror#cienciaficcion#drama', 'Una adolescente se cría bajo tierra con un robot \"Madre\", diseñado para repoblar la tierra tras la extinción de la humanidad. Pero su vínculo único se ve amenazado cuando un extraño inexplicable llega con noticias alarmantes.', 'https://m.media-amazon.com/images/M/MV5BMTkxMTczNTA4Nl5BMl5BanBnXkFtZTgwNDAyMzgwODM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(29, 'Nosotros ', 'Horror', '2019', '#misterio#thriller#horror', 'Las serenas vacaciones en la playa de una familia se convierten en un caos cuando sus doppelgängers aparecen y comienzan a aterrorizarlos.', 'https://m.media-amazon.com/images/M/MV5BZTliNWJhM2YtNDc1MC00YTk1LWE2MGYtZmE4M2Y5ODdlNzQzXkEyXkFqcGdeQXVyMzY0MTE3NzU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(30, 'Capitana Marvel', 'Accion', '2019', '#aventura#cienciaficcion#accion', 'Carol Danvers se convierte en uno de los héroes más poderosos del universo cuando la Tierra se ve atrapada en medio de una guerra galáctica entre dos razas alienígenas.', 'https://m.media-amazon.com/images/M/MV5BMTE0YWFmOTMtYTU2ZS00ZTIxLWE3OTEtYTNiYzBkZjViZThiXkEyXkFqcGdeQXVyODMzMzQ4OTI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(31, 'Shaft', 'Accion', '2019', '#comedia#crimen#accion', 'John Shaft Jr., un experto en seguridad cibernética con un título del MIT, solicita la ayuda de su familia para descubrir la verdad detrás de la muerte prematura de su mejor amigo.', 'https://m.media-amazon.com/images/M/MV5BNmExNGZmYzItZTMzMi00YWJjLWJkYmQtMDg5MjgzYjYyZDk1XkEyXkFqcGdeQXVyNjg3MDMxNzU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(32, 'Plan de Escape: Los Extractores', 'Accion', '2019', '#suspenso#accion', 'Después de que el experto en seguridad Ray Breslin es contratado para rescatar a la hija secuestrada de un magnate de la tecnología de Hong Kong de una formidable prisión letona, la novia de Breslin también es capturada.', 'https://m.media-amazon.com/images/M/MV5BMDQ2ZjUxMGUtMDg1Yy00ZWE4LWIyZTMtNThiN2IwZmE4ZDVkXkEyXkFqcGdeQXVyOTg4MDYyNw@@._V1_UY268_CR20,0,182,268_AL_.jpg'),
(33, 'Toy Story', 'Animacion', '1995', '#aventura#comedia#animacion', 'Una muñeca de vaquero está profundamente amenazada y celosa cuando una nueva figura de astronauta lo reemplaza como el mejor juguete en la habitación de un niño.', 'https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(34, 'Una guerra brillante', 'Biografia', '2017', '#drama#historia#biografia', 'La dramática historia de la feroz carrera entre los titanes de la electricidad Thomas Edison y George Westinghouse para determinar qué sistema eléctrico alimentaría al mundo moderno.', 'https://m.media-amazon.com/images/M/MV5BZGU0MWEzZTUtMTE2OC00MWI0LWJkMmItMGExODlmNDgwNzBiXkEyXkFqcGdeQXVyNzU2NzcyNA@@._V1_UY268_CR0,0,182,268_AL_.jpg'),
(35, 'Midway', 'Accion', '2019', '#drama#historia#accion', 'La historia de la Batalla de Midway, contada por los líderes y los marineros que la lucharon.', 'https://m.media-amazon.com/images/M/MV5BNTVhODZmYjktZmFhMS00MzY5LWExNGUtYWJkZjM2MmFkNzRiXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(36, 'Toy Story 3', 'Animacion', '2010', '#aventura#comedia#animacion', 'Los juguetes se entregan por error a una guardería en lugar del desván justo antes de que Andy se vaya a la universidad, y depende de Woody convencer a los otros juguetes de que no fueron abandonados y regresar a casa.', 'https://m.media-amazon.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_UY268_CR3,0,182,268_AL_.jpg'),
(37, 'Queen & Slim', 'Drama', '2019', '#drama', 'La primera cita de una pareja toma un giro inesperado cuando un oficial de policía los detiene.', 'https://m.media-amazon.com/images/M/MV5BNWRiY2ZhOGEtYjQ4NC00MWIxLTg3MzYtYmVmZjExZTlhZDY3XkEyXkFqcGdeQXVyNjYxMzg1MjY@._V1_UY268_CR110,0,182,268_AL_.jpg'),
(38, 'Quizás para siempre', 'Comedia', '2019', '#romance#comedia', 'Un par de amigos de la infancia terminan enamorándose cuando crecen', 'https://m.media-amazon.com/images/M/MV5BMGM2NWFjYTctZjFiYy00YzIxLThhY2QtY2UxZTNmNjdjZTU0XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(39, 'Star Wars: Episodio IX - El ascenso de Skywal', 'Accion', '2019', '#aventura#fantasia#accion', 'La resistencia sobreviviente se enfrenta a la Primera Orden una vez más en el capítulo final de la saga Skywalker.', 'https://m.media-amazon.com/images/M/MV5BNDA5YWU1MDItOWZlOS00YTljLThhYTYtMzM4MGI2NjhlMDYwXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(40, 'Los muertos no mueren', 'Comedia', '2019', '#fantasia#horror#comedia', 'La apacible ciudad de Centerville se encuentra luchando contra una horda de zombis mientras los muertos comienzan a levantarse de sus tumbas.', 'https://m.media-amazon.com/images/M/MV5BZWQxZDIzNzUtZGE3MS00MGU3LTk5NjMtZGFjMDljNDlmMWE1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(41, 'Alita: Ángel de combate', 'Accion', '2019', '#aventura#cienciaficcion', 'Una mujer cyborg desactivada es revivida, pero no puede recordar nada de su vida pasada y va en una búsqueda para descubrir quién es ella.', 'https://m.media-amazon.com/images/M/MV5BNzVhMjcxYjYtOTVhOS00MzQ1LWFiNTAtZmY2ZmJjNjIxMjllXkEyXkFqcGdeQXVyNTc5OTMwOTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(42, 'Cementerio de animales', 'Horror', '2019', '#misterio#thriller#horror', 'El Dr. Louis Creed y su esposa, Rachel, se mudan de Boston a Maine rural con sus dos hijos pequeños. La pareja pronto descubrirá un misterioso cementerio escondido en las profundidades del bosque cerca de su nuevo hogar.', 'https://m.media-amazon.com/images/M/MV5BZTgxMGQwM2UtZTAxNi00M2JhLTk4ZTgtZmFlODI0NmI3ZDViXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(43, 'Toy Story 2', 'Animacion', '1999', '#aventura#comedia#animacion', 'Cuando Woody es robado por un coleccionista de juguetes, Buzz y sus amigos emprenden una misión de rescate para salvar a Woody antes de que se convierta en una propiedad de juguetes del museo con su pandilla Jessie, Capataz y Tiro al Blanco.', 'https://m.media-amazon.com/images/M/MV5BMWM5ZDcxMTYtNTEyNS00MDRkLWI3YTItNThmMGExMWY4NDIwXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(44, 'Fast & Furious Presents: Hobbs & Shaw', 'Accion', '2019', '#aventura#comedia#accion', 'El hombre de la ley Luke Hobbs y el marginado Deckard Shaw forman una alianza improbable cuando un villano genéticamente mejorado amenaza el futuro de la humanidad.', 'https://m.media-amazon.com/images/M/MV5BMTc4NzA5MTgwMl5BMl5BanBnXkFtZTgwNjA2MjIzNzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(45, 'Dumbo', 'Aventura', '2019', '#familia#fantasia', 'Un joven elefante, cuyas orejas de gran tamaño le permiten volar, ayuda a salvar a un circo en apuros, pero cuando el circo planea una nueva aventura, Dumbo y sus amigos descubren oscuros secretos debajo de su chapa brillante.', 'https://m.media-amazon.com/images/M/MV5BNjMxMDE0MDI1Ml5BMl5BanBnXkFtZTgwMzExNTU3NjM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(46, 'Hotel Bombay', 'Drama', '2018', '#historia#thriller', 'La verdadera historia del ataque terrorista del Taj Hotel en Mumbai. El personal del hotel arriesga sus vidas para mantener a todos a salvo, ya que las personas hacen sacrificios impensables para protegerse a sí mismos y a sus familias.\r\n', 'https://m.media-amazon.com/images/M/MV5BYTJlZWY2YjYtZGIxMy00MDEwLTliNzMtZGM3MDQ1NzlmNDY1XkEyXkFqcGdeQXVyNDY2MjcyOTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(47, 'Ha nacido una estrella', 'Drama', '2018', '#musica#romance', 'Un músico ayuda a un joven cantante a encontrar la fama a medida que la edad y el alcoholismo envían a su propia carrera a una espiral descendente.', 'https://m.media-amazon.com/images/M/MV5BNmE5ZmE3OGItNTdlNC00YmMxLWEzNjctYzAwOGQ5ODg0OTI0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(48, 'Joker', 'Crimen', '2019', '#drama#thriller', 'Un comediante fallido se vuelve loco y se convierte en un asesino psicopático.', 'https://m.media-amazon.com/images/M/MV5BMTcyNjU1MjQ3MF5BMl5BanBnXkFtZTgwNTk1MDA4NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(49, 'Mascotas 2', 'Animacion', '2019', '#aventura#comedia#animacion', 'Continuando la historia de Max y sus mascotas, siguiendo su vida secreta después de que sus dueños los dejen para el trabajo o la escuela todos los días.\r\n', 'https://m.media-amazon.com/images/M/MV5BMzdlMWQzZmItMDA5Ny00MGFjLTk0MDAtYjgzMmMyNTEwMzdhXkEyXkFqcGdeQXVyODQzNTE3ODc@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(50, 'Ralph rompe Internet', 'Animacion', '2018', '#aventura#comedia', 'Seis años después de los eventos de \"Wreck-It Ralph\", Ralph y Vanellope, ahora amigos, descubren un enrutador wi-fi en su arcada, llevándolos a una nueva aventura.', 'https://m.media-amazon.com/images/M/MV5BMTYyNzEyNDAzOV5BMl5BanBnXkFtZTgwNTk3NDczNjM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(51, 'Infierno bajo el agua', 'Accion', '2019', '#aventura#horror#accion', 'Una mujer joven, mientras intenta salvar a su padre durante un huracán de categoría 5, se encuentra atrapada en una casa inundada y debe luchar por su vida contra los caimanes.', 'https://m.media-amazon.com/images/M/MV5BNjQxMzYyMDItZmUyNy00MGE0LWIwYmItMTMxYmZlOGZlMTlhXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(52, 'El canto del lobo', 'Accion', '2019', '#thriller#accion', 'En un futuro cercano, un submarino francés se encuentra en una situación de crisis.', 'https://m.media-amazon.com/images/M/MV5BMTA5OWMwODctY2ZiMy00MmNmLWFiMWYtM2U2ZjFmYTA2MWQ0XkEyXkFqcGdeQXVyNTc5OTMwOTQ@._V1_UY268_CR7,0,182,268_AL_.jpg'),
(53, 'Trolls 2', 'Animacion', '2020', '#aventura#comedia#animacion', 'Secuela del éxito animado 2016.', 'https://m.media-amazon.com/images/M/MV5BMzg4MGE4ODUtYWQ4My00MTRiLWEyYmQtYWZjMzFjMmQ5MDZjXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(54, 'Booksmart', 'Comedia', '2019', '#comedia', 'En la víspera de su graduación de escuela secundaria, dos superestrellas académicas y mejores amigos se dan cuenta de que deberían haber trabajado menos y haber jugado más. Decididas a no quedarse cortas con sus compañeros, las chicas intentan meter cuatro años de diversión en una sola noche.', 'https://m.media-amazon.com/images/M/MV5BMjEzMjcxNjA2Nl5BMl5BanBnXkFtZTgwMjAxMDM2NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(55, 'John Wick (Otro día para matar)', 'Accion', '2014', '#crimen#thriller#accion', 'Un ex asesino sale de su retiro para rastrear a los mafiosos que mataron a su perro y se lo llevaron todo.', 'https://m.media-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(56, 'Spider-Man: Homecoming', 'Accion', '2017', '#aventura#cienciaficcion', 'Peter Parker equilibra su vida como un estudiante de secundaria ordinario en Queens con su superhéroe alter-ego Spider-Man, y se encuentra en el camino de una nueva amenaza que recorre los cielos de la ciudad de Nueva York.', 'https://m.media-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(57, 'Hereditario', 'Drama', '2018', '#horror#misterio#drama', 'Después de que la matriarca de la familia fallece, una familia en duelo se ve acosada por sucesos trágicos e inquietantes, y comienza a desentrañar secretos oscuros.\r\n', 'https://m.media-amazon.com/images/M/MV5BOTU5MDg3OGItZWQ1Ny00ZGVmLTg2YTUtMzBkYzQ1YWIwZjlhXkEyXkFqcGdeQXVyNTAzMTY4MDA@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(58, 'Malos tiempos en El Royale', 'Crimen', '2018', '#drama#misterio#crimen', 'Alrededor de 1969, varios extraños, la mayoría con un secreto para enterrar, se encuentran por casualidad en El Royale de Lake Tahoe, un hotel en ruinas con un pasado oscuro. En el transcurso de una noche, todos mostrarán sus verdaderos colores, antes de que todo se vaya al infierno.', 'https://m.media-amazon.com/images/M/MV5BOTk1Nzk1MDc1MF5BMl5BanBnXkFtZTgwNjU2NDExNjM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(59, 'El viejo y la pistola', 'Biografia', '2018', '#comedia#crimen#biografia', 'Basado en la historia real de Forrest Tucker y su audaz fuga de San Quintín a la edad de 70 años a una serie de atracos sin precedentes que confundieron a las autoridades y encantaron al público.', 'https://m.media-amazon.com/images/M/MV5BOTk3NjU5MjIxM15BMl5BanBnXkFtZTgwNjU0OTU2NTM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(60, 'It: Capítulo 2', 'Horror', '2019', '#thriller#horror', 'Veintisiete años después de su primer encuentro con el aterrador Pennywise, el Club de Perdedores ha crecido y se ha mudado, hasta que una devastadora llamada telefónica los regresa.', 'https://m.media-amazon.com/images/M/MV5BNDlhMWY0NzYtMGQ4Yi00ZWFhLTkwZTctMGVjZDA0MTA5N2I5XkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(61, 'Little Women', 'Drama', '2019', '#romance#drama', 'Cuatro hermanas alcanzan la mayoría de edad en América después de la Guerra Civil.', 'https://m.media-amazon.com/images/M/MV5BNWI2NDQ2ZDAtNjZmZS00YWRjLWI5ZjEtMjhlMjM2NDczYTU2XkEyXkFqcGdeQXVyMzYwMDUwMTQ@._V1_UY268_CR98,0,182,268_AL_.jpg'),
(62, 'A dos metros de ti', 'Drama', '2019', '#romance#drama', 'Un par de adolescentes con fibrosis quística se encuentran en un hospital y se enamoran, aunque su enfermedad significa que deben evitar el contacto físico cercano.', 'https://m.media-amazon.com/images/M/MV5BNzVmMjJlN2MtNWQ4Ny00Zjc2LWJjYTgtYjJiNGM5MTM1ZTlkXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(63, 'Vengadores: Infinity War', 'Accion', '2018', '#aventura#cienciaficcion#accion', 'Los Vengadores y sus aliados deben estar dispuestos a sacrificar todo en un intento por derrotar al poderoso Thanos antes de que su ataque de devastación y ruina ponga fin al universo.', 'https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(64, 'Extremadamente cruel, malvado y perverso', 'Biografia', '2019', '#crimen#drama#biografia', 'Un frenesí de sala de tribunal sobreviene y barre los Estados Unidos de los años 70 cuando una joven madre soltera se encuentra con Ted Bundy .', 'https://m.media-amazon.com/images/M/MV5BMjM4ZjY5ZmQtNjUwYi00Yzk2LWIwNmMtYTg1NmU0MWExZTMzXkEyXkFqcGdeQXVyMTg2MDEyMzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(65, 'Pokémon: Detective Pikachu', 'Accion', '2019', '#aventura#comedia#accion', 'En un mundo donde las personas recolectan Pokémon para luchar, un niño se encuentra con un Pikachu inteligente que habla y busca ser un detective.', 'https://m.media-amazon.com/images/M/MV5BNDU4Mzc3NzE5NV5BMl5BanBnXkFtZTgwMzE1NzI1NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(66, 'Bohemian Rhapsody', 'Biografia', '2018', '#drama#musica#biografia', 'La historia de la legendaria banda de rock Queen y el cantante Freddie Mercury , que culminaron su famosa actuación en Live Aid', 'https://m.media-amazon.com/images/M/MV5BMTA2NDc3Njg5NDVeQTJeQWpwZ15BbWU4MDc1NDcxNTUz._V1_UX182_CR0,0,182,268_AL_.jpg'),
(67, 'El día que vendrá', 'Drama', '2019', '#romance#guerra#drama', 'Después de la Segunda Guerra Mundial, un coronel británico y su esposa fueron asignados a vivir en Hamburgo durante la reconstrucción de la posguerra, pero surgen tensiones con el alemán que anteriormente era propietario de la casa.', 'https://m.media-amazon.com/images/M/MV5BMTk2MDEyNTE5M15BMl5BanBnXkFtZTgwMzY1NDM4NjM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(68, 'Beats', 'Drama', '2019', '#drama', 'Un joven talentoso que sufrió la pérdida de su hermana se encuentra con un gerente desorientado que está tratando de volver a encarrilarse en su carrera musical.', 'https://m.media-amazon.com/images/M/MV5BZTM5ZDQ3MTctYTlmNC00OWU4LTg4MDAtM2I5NzNhM2JkOTkzXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(69, 'Doctor Sueño', 'Horror', '2019', '#horror', 'Años después de los eventos de \"The Shining\", Dan Torrence, ahora adulto, se encuentra con una joven con poderes similares a los suyos y trata de protegerla de un culto conocido como The True Knot, que se aprovecha de los niños con poderes para permanecer inmortal.', 'https://m.media-amazon.com/images/M/MV5BMzQ5MjA0ZTAtYzhkYy00NTlmLWE4YTgtMTA2ZTE5NjRjNDA2XkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(70, 'Parásitos', 'Drama', '2019', '#thriller#drama', 'Todos desempleados, la familia de Ki-taek se interesa especialmente en los parques ricos y glamorosos para su subsistencia hasta que se enredan en un incidente inesperado.', 'https://m.media-amazon.com/images/M/MV5BMjU1MTA3MzA2MV5BMl5BanBnXkFtZTgwNTUxMjQ4NzM@._V1_UY268_CR3,0,182,268_AL_.jpg'),
(71, 'Stuber', 'Accion', '2019', '#comedia#accion', 'n detective recluta a su conductor de Uber en una inesperada noche de aventuras.', 'https://m.media-amazon.com/images/M/MV5BOGE1ZjFhYzAtYWM4ZC00NGI1LWFmYzMtZWRhZDhjMjE4YzBjXkEyXkFqcGdeQXVyODQzNTE3ODc@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(72, 'Nación cautiva', 'Ciencia Ficcion', '2019', '#thriller#cienciaficcion', 'Ubicado en un vecindario de Chicago casi una década después de una ocupación por parte de una fuerza extraterrestre, el \'Estado cautivo\' explora las vidas de ambos lados del conflicto: los colaboradores y los disidentes.', 'https://m.media-amazon.com/images/M/MV5BMTgyNjU0NTAxOV5BMl5BanBnXkFtZTgwNTc4MDIzNjM@._V1_UX182_CR0,0,182,268_AL_.jpg');

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

<<<<<<< HEAD
=======
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
(91, 1, 9, 1);

>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
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
<<<<<<< HEAD
(1, 'Braiunito', 'mypass123', 'braiantablet@gmail.com', NULL);
=======
(1, 'Braiunito', 'mypass123', 'braiantablet@gmail.com', NULL),
(2, 'Agustin', '12345678', NULL, NULL),
(3, 'Marcos', '12345678', NULL, NULL),
(4, 'Mateo', '12345678', NULL, NULL),
(5, 'aber', '12345678', NULL, NULL);
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`idpeliculas`);

--
-- Indices de la tabla `relacionusuariopelis`
--
ALTER TABLE `relacionusuariopelis`
  ADD PRIMARY KEY (`IdRelacion`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  MODIFY `idpeliculas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT de la tabla `relacionusuariopelis`
--
ALTER TABLE `relacionusuariopelis`
<<<<<<< HEAD
  MODIFY `IdRelacion` int(11) NOT NULL AUTO_INCREMENT;
=======
  MODIFY `IdRelacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=220;
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
<<<<<<< HEAD
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
=======
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `relacionusuariopelis`
--
ALTER TABLE `relacionusuariopelis`
  ADD CONSTRAINT `relacionusuariopelis_ibfk_1` FOREIGN KEY (`IdPeli`) REFERENCES `peliculas` (`idpeliculas`),
  ADD CONSTRAINT `relacionusuariopelis_ibfk_2` FOREIGN KEY (`IdUsuario`) REFERENCES `usuario` (`idusuario`);
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

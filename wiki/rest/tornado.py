import tornado.ioloop
import tornado.web


class ExampleHandler(tornado.web.RequestHandler):
    """
        Class containing REST API handler functions.
    """

    def get(self) -> None:
        """
        Handles the get request for this handler.
        """
        self.write("Hola mi amigos!")


def make_app() -> tornado.web.Application:
    """
    Returns the created tornado application with all the routes registered with their appropriate handlers.
    :return: Created tornado application.
    """
    return tornado.web.Application(
        [
            (r"/", ExampleHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    # Ask the web server to listen to port 8888 for incoming requests.
    app.listen(8888)
    # Start the web service.
    tornado.ioloop.IOLoop.current().start()
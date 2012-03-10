void glActiveTexture ( GLenum texture )
void glAlphaFunc ( GLenum func, GLclampf ref )
void glAlphaFuncx ( GLenum func, GLclampx ref )
void glBindTexture ( GLenum target, GLuint texture )
void glBlendFunc ( GLenum sfactor, GLenum dfactor )
void glClear ( GLbitfield mask )
void glClearColor ( GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha )
void glClearColorx ( GLclampx red, GLclampx green, GLclampx blue, GLclampx alpha )
void glClearDepthf ( GLclampf depth )
void glClearDepthx ( GLclampx depth )
void glClearStencil ( GLint s )
void glClientActiveTexture ( GLenum texture )
void glColor4f ( GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha )
void glColor4x ( GLfixed red, GLfixed green, GLfixed blue, GLfixed alpha )
void glColorMask ( GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha )
void glColorPointer ( GLint size, GLenum type, GLsizei stride, const GLvoid *pointer )
void glCompressedTexImage2D ( GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid *data )
void glCompressedTexSubImage2D ( GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid *data )
void glCopyTexImage2D ( GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border )
void glCopyTexSubImage2D ( GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height )
void glCullFace ( GLenum mode )
void glDeleteTextures ( GLsizei n, const GLuint *textures )
void glDepthFunc ( GLenum func )
void glDepthMask ( GLboolean flag )
void glDepthRangef ( GLclampf zNear, GLclampf zFar )
void glDepthRangex ( GLclampx zNear, GLclampx zFar )
void glDisable ( GLenum cap )
void glDisableClientState ( GLenum array )
void glDrawArrays ( GLenum mode, GLint first, GLsizei count )
void glDrawElements ( GLenum mode, GLsizei count, GLenum type, const GLvoid *indices )
void glEnable ( GLenum cap )
void glEnableClientState ( GLenum array )
void glFinish ( void )
void glFlush ( void )
void glFogf ( GLenum pname, GLfloat param )
void glFogfv ( GLenum pname, const GLfloat *params )
void glFogx ( GLenum pname, GLfixed param )
void glFogxv ( GLenum pname, const GLfixed *params )
void glFrontFace ( GLenum mode )
void glFrustumf ( GLfloat left, GLfloat right, GLfloat bottom, GLfloat top, GLfloat zNear, GLfloat zFar )
void glFrustumx ( GLfixed left, GLfixed right, GLfixed bottom, GLfixed top, GLfixed zNear, GLfixed zFar )
void glGenTextures ( GLsizei n, GLuint *textures )
GLenum glGetError ( void )
void glGetIntegerv ( GLenum pname, GLint *params )
const GLubyte * glGetString ( GLenum name )
void glHint ( GLenum target, GLenum mode )
void glLightModelf ( GLenum pname, GLfloat param )
void glLightModelfv ( GLenum pname, const GLfloat *params )
void glLightModelx ( GLenum pname, GLfixed param )
void glLightModelxv ( GLenum pname, const GLfixed *params )
void glLightf ( GLenum light, GLenum pname, GLfloat param )
void glLightfv ( GLenum light, GLenum pname, const GLfloat *params )
void glLightx ( GLenum light, GLenum pname, GLfixed param )
void glLightxv ( GLenum light, GLenum pname, const GLfixed *params )
void glLineWidth ( GLfloat width )
void glLineWidthx ( GLfixed width )
void glLoadIdentity ( void )
void glLoadMatrixf ( const GLfloat *m )
void glLoadMatrixx ( const GLfixed *m )
void glLogicOp ( GLenum opcode )
void glMaterialf ( GLenum face, GLenum pname, GLfloat param )
void glMaterialfv ( GLenum face, GLenum pname, const GLfloat *params )
void glMaterialx ( GLenum face, GLenum pname, GLfixed param )
void glMaterialxv ( GLenum face, GLenum pname, const GLfixed *params )
void glMatrixMode ( GLenum mode )
void glMultMatrixf ( const GLfloat *m )
void glMultMatrixx ( const GLfixed *m )
void glMultiTexCoord4f ( GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q )
void glMultiTexCoord4x ( GLenum target, GLfixed s, GLfixed t, GLfixed r, GLfixed q )
void glNormal3f ( GLfloat nx, GLfloat ny, GLfloat nz )
void glNormal3x ( GLfixed nx, GLfixed ny, GLfixed nz )
void glNormalPointer ( GLenum type, GLsizei stride, const GLvoid *pointer )
void glOrthof ( GLfloat left, GLfloat right, GLfloat bottom, GLfloat top, GLfloat zNear, GLfloat zFar )
void glOrthox ( GLfixed left, GLfixed right, GLfixed bottom, GLfixed top, GLfixed zNear, GLfixed zFar )
void glPixelStorei ( GLenum pname, GLint param )
void glPointSize ( GLfloat size )
void glPointSizex ( GLfixed size )
void glPolygonOffset ( GLfloat factor, GLfloat units )
void glPolygonOffsetx ( GLfixed factor, GLfixed units )
void glPopMatrix ( void )
void glPushMatrix ( void )
void glReadPixels ( GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels )
void glRotatef ( GLfloat angle, GLfloat x, GLfloat y, GLfloat z )
void glRotatex ( GLfixed angle, GLfixed x, GLfixed y, GLfixed z )
void glSampleCoverage ( GLclampf value, GLboolean invert )
void glSampleCoveragex ( GLclampx value, GLboolean invert )
void glScalef ( GLfloat x, GLfloat y, GLfloat z )
void glScalex ( GLfixed x, GLfixed y, GLfixed z )
void glScissor ( GLint x, GLint y, GLsizei width, GLsizei height )
void glShadeModel ( GLenum mode )
void glStencilFunc ( GLenum func, GLint ref, GLuint mask )
void glStencilMask ( GLuint mask )
void glStencilOp ( GLenum fail, GLenum zfail, GLenum zpass )
void glTexCoordPointer ( GLint size, GLenum type, GLsizei stride, const GLvoid *pointer )
void glTexEnvf ( GLenum target, GLenum pname, GLfloat param )
void glTexEnvfv ( GLenum target, GLenum pname, const GLfloat *params )
void glTexEnvx ( GLenum target, GLenum pname, GLfixed param )
void glTexEnvxv ( GLenum target, GLenum pname, const GLfixed *params )
void glTexImage2D ( GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels )
void glTexParameterf ( GLenum target, GLenum pname, GLfloat param )
void glTexParameterx ( GLenum target, GLenum pname, GLfixed param )
void glTexSubImage2D ( GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels )
void glTranslatef ( GLfloat x, GLfloat y, GLfloat z )
void glTranslatex ( GLfixed x, GLfixed y, GLfixed z )
void glVertexPointer ( GLint size, GLenum type, GLsizei stride, const GLvoid *pointer )
void glViewport ( GLint x, GLint y, GLsizei width, GLsizei height )
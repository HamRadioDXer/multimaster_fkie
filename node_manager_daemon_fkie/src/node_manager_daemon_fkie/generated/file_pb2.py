# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nfile.proto\"\x07\n\x05\x45mpty\"%\n\x15GetFileContentRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"N\n\x13GetFileContentReply\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.ReturnStatus\x12\x18\n\x04\x66ile\x18\x02 \x01(\x0b\x32\n.FileChunk\")\n\rRenameRequest\x12\x0b\n\x03old\x18\x01 \x01(\t\x12\x0b\n\x03new\x18\x02 \x01(\t\"E\n\x16SaveFileContentRequest\x12\x11\n\toverwrite\x18\x01 \x01(\x08\x12\x18\n\x04\x66ile\x18\x02 \x01(\x0b\x32\n.FileChunk\"Q\n\x14SaveFileContentReply\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.ReturnStatus\x12\x1a\n\x03\x61\x63k\x18\x02 \x01(\x0b\x32\r.FileChunkAck\"=\n\rCopyToRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\toverwrite\x18\x03 \x01(\x08\"e\n\tFileChunk\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x01\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0e\n\x06offset\x18\x04 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\x0f\n\x07package\x18\x06 \x01(\t\"9\n\x0c\x46ileChunkAck\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x01\x12\x0c\n\x04size\x18\x04 \x01(\x04\"\x1f\n\x0fListPathRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"U\n\rListPathReply\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.ReturnStatus\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\x05items\x18\x03 \x03(\x0b\x32\x08.PathObj\"#\n\x08PathList\x12\x17\n\x05items\x18\x01 \x03(\x0b\x32\x08.PathObj\"\x8e\x01\n\x07PathObj\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x01\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x1f\n\x04type\x18\x04 \x01(\x0e\x32\x11.PathObj.PathType\"7\n\x08PathType\x12\x08\n\x04\x46ILE\x10\x00\x12\x07\n\x03\x44IR\x10\x01\x12\x0b\n\x07SYMLINK\x10\x02\x12\x0b\n\x07PACKAGE\x10\x03\"\xb8\x01\n\x0cReturnStatus\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x11\n\terror_msg\x18\x03 \x01(\t\x12\x12\n\nerror_file\x18\x04 \x01(\t\"_\n\nStatusType\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0c\n\x08IO_ERROR\x10\x02\x12\x0c\n\x08OS_ERROR\x10\x03\x12\x10\n\x0c\x43HANGED_FILE\x10\x04\x12\x10\n\x0cREMOVED_FILE\x10\x05\".\n\x13ListPackagesRequest\x12\x17\n\x0f\x63lear_ros_cache\x18\x01 \x01(\x08\"N\n\x11ListPackagesReply\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.ReturnStatus\x12\x1a\n\x05items\x18\x02 \x03(\x0b\x32\x0b.PackageObj\"(\n\nPackageObj\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t2\xa8\x03\n\x0b\x46ileService\x12@\n\x0eGetFileContent\x12\x16.GetFileContentRequest\x1a\x14.GetFileContentReply0\x01\x12\x45\n\x0fSaveFileContent\x12\x17.SaveFileContentRequest\x1a\x15.SaveFileContentReply(\x01\x30\x01\x12+\n\nCopyFileTo\x12\x0e.CopyToRequest\x1a\r.ReturnStatus\x12\'\n\x06Rename\x12\x0e.RenameRequest\x1a\r.ReturnStatus\x12,\n\x08ListPath\x12\x10.ListPathRequest\x1a\x0e.ListPathReply\x12\x38\n\x0cListPackages\x12\x14.ListPackagesRequest\x1a\x12.ListPackagesReply\x12$\n\x0c\x43hangedFiles\x12\t.PathList\x1a\t.PathList\x12,\n\x12GetPackageBinaries\x12\x0b.PackageObj\x1a\t.PathListb\x06proto3')
)



_PATHOBJ_PATHTYPE = _descriptor.EnumDescriptor(
  name='PathType',
  full_name='PathObj.PathType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMLINK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=809,
  serialized_end=864,
)
_sym_db.RegisterEnumDescriptor(_PATHOBJ_PATHTYPE)

_RETURNSTATUS_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='ReturnStatus.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IO_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OS_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGED_FILE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED_FILE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=956,
  serialized_end=1051,
)
_sym_db.RegisterEnumDescriptor(_RETURNSTATUS_STATUSTYPE)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=21,
)


_GETFILECONTENTREQUEST = _descriptor.Descriptor(
  name='GetFileContentRequest',
  full_name='GetFileContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='GetFileContentRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=60,
)


_GETFILECONTENTREPLY = _descriptor.Descriptor(
  name='GetFileContentReply',
  full_name='GetFileContentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='GetFileContentReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='GetFileContentReply.file', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=140,
)


_RENAMEREQUEST = _descriptor.Descriptor(
  name='RenameRequest',
  full_name='RenameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old', full_name='RenameRequest.old', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new', full_name='RenameRequest.new', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=183,
)


_SAVEFILECONTENTREQUEST = _descriptor.Descriptor(
  name='SaveFileContentRequest',
  full_name='SaveFileContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='SaveFileContentRequest.overwrite', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='SaveFileContentRequest.file', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=254,
)


_SAVEFILECONTENTREPLY = _descriptor.Descriptor(
  name='SaveFileContentReply',
  full_name='SaveFileContentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SaveFileContentReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack', full_name='SaveFileContentReply.ack', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=337,
)


_COPYTOREQUEST = _descriptor.Descriptor(
  name='CopyToRequest',
  full_name='CopyToRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='CopyToRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='CopyToRequest.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='CopyToRequest.overwrite', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=400,
)


_FILECHUNK = _descriptor.Descriptor(
  name='FileChunk',
  full_name='FileChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='FileChunk.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='FileChunk.mtime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='FileChunk.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='FileChunk.offset', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='FileChunk.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package', full_name='FileChunk.package', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=503,
)


_FILECHUNKACK = _descriptor.Descriptor(
  name='FileChunkAck',
  full_name='FileChunkAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='FileChunkAck.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='FileChunkAck.mtime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='FileChunkAck.size', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=562,
)


_LISTPATHREQUEST = _descriptor.Descriptor(
  name='ListPathRequest',
  full_name='ListPathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='ListPathRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=595,
)


_LISTPATHREPLY = _descriptor.Descriptor(
  name='ListPathReply',
  full_name='ListPathReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ListPathReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='ListPathReply.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='ListPathReply.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=682,
)


_PATHLIST = _descriptor.Descriptor(
  name='PathList',
  full_name='PathList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='PathList.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=719,
)


_PATHOBJ = _descriptor.Descriptor(
  name='PathObj',
  full_name='PathObj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='PathObj.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='PathObj.mtime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='PathObj.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='PathObj.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PATHOBJ_PATHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=864,
)


_RETURNSTATUS = _descriptor.Descriptor(
  name='ReturnStatus',
  full_name='ReturnStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ReturnStatus.code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='ReturnStatus.error_code', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='ReturnStatus.error_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_file', full_name='ReturnStatus.error_file', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RETURNSTATUS_STATUSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=1051,
)


_LISTPACKAGESREQUEST = _descriptor.Descriptor(
  name='ListPackagesRequest',
  full_name='ListPackagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clear_ros_cache', full_name='ListPackagesRequest.clear_ros_cache', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1053,
  serialized_end=1099,
)


_LISTPACKAGESREPLY = _descriptor.Descriptor(
  name='ListPackagesReply',
  full_name='ListPackagesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ListPackagesReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='ListPackagesReply.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1101,
  serialized_end=1179,
)


_PACKAGEOBJ = _descriptor.Descriptor(
  name='PackageObj',
  full_name='PackageObj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PackageObj.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='PackageObj.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1181,
  serialized_end=1221,
)

_GETFILECONTENTREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_GETFILECONTENTREPLY.fields_by_name['file'].message_type = _FILECHUNK
_SAVEFILECONTENTREQUEST.fields_by_name['file'].message_type = _FILECHUNK
_SAVEFILECONTENTREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_SAVEFILECONTENTREPLY.fields_by_name['ack'].message_type = _FILECHUNKACK
_LISTPATHREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_LISTPATHREPLY.fields_by_name['items'].message_type = _PATHOBJ
_PATHLIST.fields_by_name['items'].message_type = _PATHOBJ
_PATHOBJ.fields_by_name['type'].enum_type = _PATHOBJ_PATHTYPE
_PATHOBJ_PATHTYPE.containing_type = _PATHOBJ
_RETURNSTATUS_STATUSTYPE.containing_type = _RETURNSTATUS
_LISTPACKAGESREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_LISTPACKAGESREPLY.fields_by_name['items'].message_type = _PACKAGEOBJ
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['GetFileContentRequest'] = _GETFILECONTENTREQUEST
DESCRIPTOR.message_types_by_name['GetFileContentReply'] = _GETFILECONTENTREPLY
DESCRIPTOR.message_types_by_name['RenameRequest'] = _RENAMEREQUEST
DESCRIPTOR.message_types_by_name['SaveFileContentRequest'] = _SAVEFILECONTENTREQUEST
DESCRIPTOR.message_types_by_name['SaveFileContentReply'] = _SAVEFILECONTENTREPLY
DESCRIPTOR.message_types_by_name['CopyToRequest'] = _COPYTOREQUEST
DESCRIPTOR.message_types_by_name['FileChunk'] = _FILECHUNK
DESCRIPTOR.message_types_by_name['FileChunkAck'] = _FILECHUNKACK
DESCRIPTOR.message_types_by_name['ListPathRequest'] = _LISTPATHREQUEST
DESCRIPTOR.message_types_by_name['ListPathReply'] = _LISTPATHREPLY
DESCRIPTOR.message_types_by_name['PathList'] = _PATHLIST
DESCRIPTOR.message_types_by_name['PathObj'] = _PATHOBJ
DESCRIPTOR.message_types_by_name['ReturnStatus'] = _RETURNSTATUS
DESCRIPTOR.message_types_by_name['ListPackagesRequest'] = _LISTPACKAGESREQUEST
DESCRIPTOR.message_types_by_name['ListPackagesReply'] = _LISTPACKAGESREPLY
DESCRIPTOR.message_types_by_name['PackageObj'] = _PACKAGEOBJ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)

GetFileContentRequest = _reflection.GeneratedProtocolMessageType('GetFileContentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFILECONTENTREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:GetFileContentRequest)
  ))
_sym_db.RegisterMessage(GetFileContentRequest)

GetFileContentReply = _reflection.GeneratedProtocolMessageType('GetFileContentReply', (_message.Message,), dict(
  DESCRIPTOR = _GETFILECONTENTREPLY,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:GetFileContentReply)
  ))
_sym_db.RegisterMessage(GetFileContentReply)

RenameRequest = _reflection.GeneratedProtocolMessageType('RenameRequest', (_message.Message,), dict(
  DESCRIPTOR = _RENAMEREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:RenameRequest)
  ))
_sym_db.RegisterMessage(RenameRequest)

SaveFileContentRequest = _reflection.GeneratedProtocolMessageType('SaveFileContentRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVEFILECONTENTREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:SaveFileContentRequest)
  ))
_sym_db.RegisterMessage(SaveFileContentRequest)

SaveFileContentReply = _reflection.GeneratedProtocolMessageType('SaveFileContentReply', (_message.Message,), dict(
  DESCRIPTOR = _SAVEFILECONTENTREPLY,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:SaveFileContentReply)
  ))
_sym_db.RegisterMessage(SaveFileContentReply)

CopyToRequest = _reflection.GeneratedProtocolMessageType('CopyToRequest', (_message.Message,), dict(
  DESCRIPTOR = _COPYTOREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:CopyToRequest)
  ))
_sym_db.RegisterMessage(CopyToRequest)

FileChunk = _reflection.GeneratedProtocolMessageType('FileChunk', (_message.Message,), dict(
  DESCRIPTOR = _FILECHUNK,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:FileChunk)
  ))
_sym_db.RegisterMessage(FileChunk)

FileChunkAck = _reflection.GeneratedProtocolMessageType('FileChunkAck', (_message.Message,), dict(
  DESCRIPTOR = _FILECHUNKACK,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:FileChunkAck)
  ))
_sym_db.RegisterMessage(FileChunkAck)

ListPathRequest = _reflection.GeneratedProtocolMessageType('ListPathRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPATHREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:ListPathRequest)
  ))
_sym_db.RegisterMessage(ListPathRequest)

ListPathReply = _reflection.GeneratedProtocolMessageType('ListPathReply', (_message.Message,), dict(
  DESCRIPTOR = _LISTPATHREPLY,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:ListPathReply)
  ))
_sym_db.RegisterMessage(ListPathReply)

PathList = _reflection.GeneratedProtocolMessageType('PathList', (_message.Message,), dict(
  DESCRIPTOR = _PATHLIST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:PathList)
  ))
_sym_db.RegisterMessage(PathList)

PathObj = _reflection.GeneratedProtocolMessageType('PathObj', (_message.Message,), dict(
  DESCRIPTOR = _PATHOBJ,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:PathObj)
  ))
_sym_db.RegisterMessage(PathObj)

ReturnStatus = _reflection.GeneratedProtocolMessageType('ReturnStatus', (_message.Message,), dict(
  DESCRIPTOR = _RETURNSTATUS,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:ReturnStatus)
  ))
_sym_db.RegisterMessage(ReturnStatus)

ListPackagesRequest = _reflection.GeneratedProtocolMessageType('ListPackagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKAGESREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:ListPackagesRequest)
  ))
_sym_db.RegisterMessage(ListPackagesRequest)

ListPackagesReply = _reflection.GeneratedProtocolMessageType('ListPackagesReply', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKAGESREPLY,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:ListPackagesReply)
  ))
_sym_db.RegisterMessage(ListPackagesReply)

PackageObj = _reflection.GeneratedProtocolMessageType('PackageObj', (_message.Message,), dict(
  DESCRIPTOR = _PACKAGEOBJ,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:PackageObj)
  ))
_sym_db.RegisterMessage(PackageObj)



_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='FileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1224,
  serialized_end=1648,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFileContent',
    full_name='FileService.GetFileContent',
    index=0,
    containing_service=None,
    input_type=_GETFILECONTENTREQUEST,
    output_type=_GETFILECONTENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SaveFileContent',
    full_name='FileService.SaveFileContent',
    index=1,
    containing_service=None,
    input_type=_SAVEFILECONTENTREQUEST,
    output_type=_SAVEFILECONTENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CopyFileTo',
    full_name='FileService.CopyFileTo',
    index=2,
    containing_service=None,
    input_type=_COPYTOREQUEST,
    output_type=_RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Rename',
    full_name='FileService.Rename',
    index=3,
    containing_service=None,
    input_type=_RENAMEREQUEST,
    output_type=_RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPath',
    full_name='FileService.ListPath',
    index=4,
    containing_service=None,
    input_type=_LISTPATHREQUEST,
    output_type=_LISTPATHREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPackages',
    full_name='FileService.ListPackages',
    index=5,
    containing_service=None,
    input_type=_LISTPACKAGESREQUEST,
    output_type=_LISTPACKAGESREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangedFiles',
    full_name='FileService.ChangedFiles',
    index=6,
    containing_service=None,
    input_type=_PATHLIST,
    output_type=_PATHLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPackageBinaries',
    full_name='FileService.GetPackageBinaries',
    index=7,
    containing_service=None,
    input_type=_PACKAGEOBJ,
    output_type=_PATHLIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)
